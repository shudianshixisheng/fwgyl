/**
 * API 接口服务
 * Base URL: https://cuizy.online/lsszjj
 */

const BASE_URL = 'https://cuizy.online/lsszjj'

// 获取存储的token
const getToken = () => localStorage.getItem('access_token')

// 通用请求方法
const request = async (url, options = {}) => {
  const headers = {
    'Content-Type': 'application/json',
    ...options.headers
  }
  
  // 如果需要认证，添加token
  if (options.auth !== false) {
    const token = getToken()
    if (token) {
      headers['Authorization'] = `Bearer ${token}`
    }
  }
  
  try {
    const response = await fetch(`${BASE_URL}${url}`, {
      ...options,
      headers
    })
    
    const data = await response.json()
    
    // 处理403错误（token无效）
    if (data.code === 403) {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('userInfo')
      throw new Error(data.message || '登录已过期，请重新登录')
    }
    
    return data
  } catch (error) {
    console.error('API请求错误:', error)
    throw error
  }
}

/**
 * 密码登录
 * @param {string} username - 手机号
 * @param {string} password - 密码
 */
export const login = async (username, password) => {
  const data = await request('/auth/login', {
    method: 'POST',
    auth: false,
    body: JSON.stringify({
      username,
      password,
      method: '0',  // 密码登录
      platform: '0' // PC平台
    })
  })
  
  if (data.code === 200) {
    // 保存token
    localStorage.setItem('access_token', data.data.access_token)
    localStorage.setItem('refresh_token', data.data.refresh_token)
  }
  
  return data
}

/**
 * 短信验证码登录
 * @param {string} username - 手机号
 * @param {string} smsCode - 验证码
 */
export const loginWithSms = async (username, smsCode) => {
  const data = await request('/auth/login', {
    method: 'POST',
    auth: false,
    body: JSON.stringify({
      username,
      password: smsCode,
      method: '1',  // 短信登录
      platform: '0' // PC平台
    })
  })
  
  if (data.code === 200) {
    // 保存token
    localStorage.setItem('access_token', data.data.access_token)
    localStorage.setItem('refresh_token', data.data.refresh_token)
  }
  
  return data
}

/**
 * 发送短信验证码
 * @param {string} phone - 手机号
 * @param {number} type - 类型：1-注册验证码, 0-登录验证码
 */
export const sendSms = async (phone, type = 1) => {
  return request(`/auth/sms/send?phone=${phone}&type=${type}`, {
    method: 'POST',
    auth: false,
    body: JSON.stringify({})
  })
}

/**
 * 发送登录验证码
 * @param {string} phone - 手机号
 */
export const sendLoginSms = async (phone) => {
  return request(`/auth/sms/send?phone=${phone}&type=0`, {
    method: 'POST',
    auth: false,
    body: JSON.stringify({})
  })
}

/**
 * 注册接口
 * @param {object} params - 注册参数
 */
export const register = async (params) => {
  const data = await request('/auth/register', {
    method: 'POST',
    auth: false,
    body: JSON.stringify({
      phone: params.phone,
      email: params.email || '',
      gender: params.gender || '0',
      sms_code: params.smsCode,
      password: params.password,
      password_two: params.passwordTwo || params.password
    })
  })
  
  return data
}

/**
 * 获取当前用户信息
 */
export const getCurrentUser = async () => {
  return request('/user/user/current/info', {
    method: 'GET'
  })
}

/**
 * 更新个人信息
 * @param {object} params - 更新参数
 */
export const updateProfile = async (params) => {
  return request('/user/profile/update', {
    method: 'PUT',
    body: JSON.stringify(params)
  })
}

/**
 * 实名认证
 * @param {string} name - 真实姓名
 * @param {string} idcard - 身份证号
 */
export const verifyIdcard = async (name, idcard) => {
  return request('/user/verify/idcard', {
    method: 'POST',
    body: JSON.stringify({ name, idcard })
  })
}

/**
 * 获取实名认证状态
 */
export const getVerifyStatus = async () => {
  return request('/user/verify/status', {
    method: 'GET'
  })
}

export default {
  login,
  sendSms,
  register,
  getCurrentUser,
  updateProfile,
  verifyIdcard,
  getVerifyStatus
}
