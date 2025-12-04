import { ref, computed } from 'vue'
import * as api from '../api/index.js'
import { loginWithSms as apiLoginWithSms, sendLoginSms as apiSendLoginSms } from '../api/index.js'

// 用户信息
const userInfo = ref(null)
// 实名认证信息
const verifyInfo = ref(null)
// 加载状态
const loading = ref(false)

// 从 localStorage 恢复用户信息
if (localStorage.getItem('userInfo')) {
  try {
    userInfo.value = JSON.parse(localStorage.getItem('userInfo'))
  } catch (e) {
    console.error('恢复用户信息失败:', e)
  }
}

export function useAuth() {
  // 是否已登录
  const isLoggedIn = computed(() => !!userInfo.value && !!localStorage.getItem('access_token'))
  
  // 是否已实名
  const isVerified = computed(() => verifyInfo.value?.is_verified || false)
  
  // 用户等级（金码/银码）
  const userLevel = computed(() => {
    if (!userInfo.value) return null
    return userInfo.value.level || 'gold' // 默认金码
  })
  
  // 用户等级文本
  const userLevelText = computed(() => {
    if (!isLoggedIn.value) return ''
    return userLevel.value === 'gold' ? '金码用户' : '银码用户'
  })
  
  // 登录（密码登录）
  const loginWithPassword = async (phone, password) => {
    loading.value = true
    try {
      const res = await api.login(phone, password)
      if (res.code === 200) {
        // 获取用户信息
        await fetchUserInfo()
        return { success: true, data: res.data }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message || '登录失败' }
    } finally {
      loading.value = false
    }
  }
  
  // 登录（短信验证码登录）
  const loginWithSms = async (phone, smsCode) => {
    loading.value = true
    try {
      const res = await apiLoginWithSms(phone, smsCode)
      if (res.code === 200) {
        // 获取用户信息
        await fetchUserInfo()
        return { success: true, data: res.data }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message || '登录失败' }
    } finally {
      loading.value = false
    }
  }
  
  // 发送注册验证码
  const sendSmsCode = async (phone) => {
    try {
      const res = await api.sendSms(phone, 1)
      if (res.code === 200) {
        return { success: true }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message || '发送失败' }
    }
  }
  
  // 发送登录验证码
  const sendLoginSmsCode = async (phone) => {
    try {
      const res = await apiSendLoginSms(phone)
      if (res.code === 200) {
        return { success: true }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message || '发送失败' }
    }
  }
  
  // 注册
  const registerUser = async (params) => {
    loading.value = true
    try {
      const res = await api.register(params)
      if (res.code === 200) {
        return { success: true, data: res.data }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message || '注册失败' }
    } finally {
      loading.value = false
    }
  }
  
  // 获取用户信息
  const fetchUserInfo = async () => {
    try {
      const res = await api.getCurrentUser()
      if (res.code === 200) {
        userInfo.value = res.data
        localStorage.setItem('userInfo', JSON.stringify(res.data))
        // 同时获取实名状态
        await fetchVerifyStatus()
        return { success: true, data: res.data }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message }
    }
  }
  
  // 获取实名状态
  const fetchVerifyStatus = async () => {
    try {
      const res = await api.getVerifyStatus()
      if (res.code === 200) {
        verifyInfo.value = res.data
        return { success: true, data: res.data }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message }
    }
  }
  
  // 实名认证
  const verifyIdcard = async (name, idcard) => {
    loading.value = true
    try {
      const res = await api.verifyIdcard(name, idcard)
      if (res.code === 200) {
        // 刷新实名状态
        await fetchVerifyStatus()
        return { success: true, data: res.data }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message || '认证失败' }
    } finally {
      loading.value = false
    }
  }
  
  // 更新个人信息
  const updateProfile = async (params) => {
    loading.value = true
    try {
      const res = await api.updateProfile(params)
      if (res.code === 200) {
        userInfo.value = res.data
        localStorage.setItem('userInfo', JSON.stringify(res.data))
        return { success: true, data: res.data }
      } else {
        return { success: false, message: res.message }
      }
    } catch (error) {
      return { success: false, message: error.message || '更新失败' }
    } finally {
      loading.value = false
    }
  }
  
  // 登出
  const logout = () => {
    userInfo.value = null
    verifyInfo.value = null
    localStorage.removeItem('userInfo')
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  }
  
  return {
    userInfo,
    verifyInfo,
    loading,
    isLoggedIn,
    isVerified,
    userLevel,
    userLevelText,
    loginWithPassword,
    loginWithSms,
    sendSmsCode,
    sendLoginSmsCode,
    registerUser,
    fetchUserInfo,
    fetchVerifyStatus,
    verifyIdcard,
    updateProfile,
    logout
  }
}

