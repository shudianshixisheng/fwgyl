<template>
  <div class="login-page">
    <!-- 复用通用头部导航 -->
    <AppHeader />

    <!-- 主体内容 -->
    <main class="main-content">
      <div class="content-wrapper">
        <!-- 左侧信息区域 -->
        <div class="info-section">
          <h1 class="main-title">陵水好房码</h1>
          <p class="main-subtitle">极速现房交易平台</p>
          
          <!-- 特性列表 -->
          <div class="features">
            <div class="feature-item">
              <div class="feature-icon blue">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
                </svg>
              </div>
              <div class="feature-text">
                <h3 class="feature-title">两保两真</h3>
                <p class="feature-desc">政府信用背书，房源真实可靠</p>
              </div>
            </div>
            
            <div class="feature-item">
              <div class="feature-icon purple">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="5" height="5" x="3" y="3" rx="1"></rect>
                  <rect width="5" height="5" x="16" y="3" rx="1"></rect>
                  <rect width="5" height="5" x="3" y="16" rx="1"></rect>
                  <path d="M21 16h-3a2 2 0 0 0-2 2v3"></path>
                  <path d="M21 21v.01"></path>
                  <path d="M12 7v3a2 2 0 0 1-2 2H7"></path>
                  <path d="M3 12h.01"></path>
                  <path d="M12 3h.01"></path>
                  <path d="M12 16v.01"></path>
                  <path d="M16 12h1"></path>
                  <path d="M21 12v.01"></path>
                  <path d="M12 21v-1"></path>
                </svg>
              </div>
              <div class="feature-text">
                <h3 class="feature-title">一码勿扰</h3>
                <p class="feature-desc">隐私保护，无骚扰购房体验</p>
              </div>
            </div>
            
            <div class="feature-item">
              <div class="feature-icon gray">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </div>
              <div class="feature-text">
                <h3 class="feature-title">定金托管</h3>
                <p class="feature-desc">24小时可退，安全有保障</p>
              </div>
            </div>
          </div>
          
          <!-- 用户等级卡片 -->
          <div class="level-card">
            <h3 class="level-title">用户好房码等级</h3>
            <div class="level-item gold">
              <span class="level-dot"></span>
              <span class="level-name">金码用户</span>
              <span class="level-desc">信用分≥700 或 已购房</span>
            </div>
            <div class="level-item silver">
              <span class="level-dot"></span>
              <span class="level-name">银码用户</span>
              <span class="level-desc">信用分600-699</span>
            </div>
          </div>
        </div>

        <!-- 右侧卡片 -->
        <!-- 步骤1：登录/注册 -->
        <div v-if="step === 1" class="login-card">
          <!-- 登录模式切换 -->
          <div class="mode-tabs">
            <button 
              type="button" 
              class="mode-tab" 
              :class="{ active: loginMode === 'password' }"
              @click="switchToPasswordLogin"
            >密码登录</button>
            <button 
              type="button" 
              class="mode-tab" 
              :class="{ active: loginMode === 'register' }"
              @click="switchToRegister"
            >注册账号</button>
          </div>
          
          <div class="card-header">
            <h2 class="card-title">{{ loginMode === 'password' ? '密码登录' : '手机号注册' }}</h2>
            <p class="card-subtitle">{{ loginMode === 'password' ? '使用已注册账号登录' : '首次登录将自动注册' }}</p>
          </div>
          
          <!-- 错误提示 -->
          <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
          
          <!-- 密码登录表单 -->
          <form v-if="loginMode === 'password'" class="login-form" @submit.prevent="handlePasswordLogin">
            <div class="form-group">
              <label class="form-label">手机号</label>
              <div class="input-wrapper">
                <svg class="input-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"></path>
                </svg>
                <input 
                  type="tel"
                  class="form-input"
                  placeholder="请输入手机号"
                  v-model="phone"
                  maxlength="11"
                />
              </div>
            </div>
            
            <!-- 密码/验证码切换 -->
            <div class="login-type-switch">
              <button type="button" :class="{ active: loginType === 'password' }" @click="loginType = 'password'">密码登录</button>
              <button type="button" :class="{ active: loginType === 'sms' }" @click="loginType = 'sms'">验证码登录</button>
            </div>
            
            <!-- 密码输入 -->
            <div v-if="loginType === 'password'" class="form-group">
              <label class="form-label">密码</label>
              <div class="input-wrapper">
                <svg class="input-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
                <input 
                  type="password"
                  class="form-input"
                  placeholder="请输入密码"
                  v-model="password"
                />
              </div>
            </div>
            
            <!-- 验证码输入 -->
            <div v-else class="form-group">
              <label class="form-label">验证码</label>
              <div class="code-input-wrapper">
                <input 
                  type="text"
                  class="form-input code-input"
                  placeholder="请输入验证码"
                  v-model="loginCode"
                  maxlength="6"
                />
                <button 
                  type="button" 
                  class="send-code-btn"
                  :disabled="countdown > 0 || loading"
                  @click="sendLoginCode"
                >
                  {{ countdown > 0 ? `${countdown}s` : '获取验证码' }}
                </button>
              </div>
            </div>
            
            <button 
              type="submit"
              class="submit-btn"
              :class="{ loading: loading }"
              :disabled="loading"
            >
              <span v-if="loading" class="loading-spinner"></span>
              <span>登录</span>
            </button>
          </form>
          
          <!-- 注册表单 -->
          <form v-else class="login-form" @submit.prevent="handleSubmit">
            <div class="form-group">
              <label class="form-label">手机号</label>
              <div class="input-wrapper">
                <svg class="input-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"></path>
                </svg>
                <input 
                  type="tel"
                  class="form-input"
                  placeholder="请输入手机号"
                  v-model="phone"
                  maxlength="11"
                />
              </div>
            </div>
            
            <button 
              type="submit"
              class="submit-btn"
              :class="{ loading: loading }"
              :disabled="loading"
            >
              <span v-if="loading" class="loading-spinner"></span>
              <span>下一步</span>
            </button>
          </form>
          
          <p class="agreement-text">
            登录即表示同意<button type="button" class="link-btn">《用户协议》</button>和<button type="button" class="link-btn">《隐私政策》</button>
          </p>
          
          <div class="security-badges">
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
              </svg>
              <span>信息加密</span>
            </div>
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
              <span>隐私保护</span>
            </div>
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21.801 10A10 10 0 1 1 17 3.335"></path>
                <path d="m9 11 3 3L22 4"></path>
              </svg>
              <span>政府监管</span>
            </div>
          </div>
        </div>

        <!-- 步骤2：验证码验证 -->
        <div v-else-if="step === 2" class="verify-card">
          <div class="card-header">
            <h2 class="card-title">验证手机号</h2>
            <p class="card-subtitle">请输入收到的验证码并设置密码</p>
          </div>
          
          <p class="phone-hint">验证码已发送至 {{ phone }}</p>
          
          <!-- 错误提示 -->
          <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
          
          <div class="verify-form">
            <input 
              type="text"
              class="verify-input"
              placeholder="请输入6位验证码"
              v-model="code"
              maxlength="6"
            />
            
            <input 
              type="email"
              class="verify-input"
              placeholder="请输入邮箱地址"
              v-model="email"
            />
            
            <input 
              type="password"
              class="verify-input"
              placeholder="请设置登录密码（至少6位）"
              v-model="password"
            />
            
            <input 
              type="password"
              class="verify-input"
              placeholder="请再次输入密码"
              v-model="passwordTwo"
            />
            
            <button 
              type="button"
              class="resend-btn"
              :class="{ disabled: countdown > 0 || loading }"
              :disabled="countdown > 0 || loading"
              @click="sendCode"
            >
              {{ countdown > 0 ? `${countdown}秒后重新发送` : '重新发送验证码' }}
            </button>
            
            <button 
              type="button"
              class="submit-btn"
              :class="{ loading: loading }"
              :disabled="loading || code.length !== 6 || !email || password.length < 6 || !passwordTwo"
              @click="handleVerify"
            >
              <span v-if="loading" class="loading-spinner"></span>
              <span>注册并登录</span>
            </button>
            
            <button type="button" class="back-btn" @click="goBack">
              返回
            </button>
          </div>
          
          <div class="divider"></div>
          
          <div class="security-badges">
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
              </svg>
              <span>信息加密</span>
            </div>
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
              <span>隐私保护</span>
            </div>
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21.801 10A10 10 0 1 1 17 3.335"></path>
                <path d="m9 11 3 3L22 4"></path>
              </svg>
              <span>政府监管</span>
            </div>
          </div>
        </div>

        <!-- 步骤3：实名认证 -->
        <div v-else-if="step === 3" class="realname-card">
          <div class="card-header">
            <h2 class="card-title">实名认证</h2>
            <p class="card-subtitle">完成实名认证，生成好房码</p>
          </div>
          
          <!-- 错误提示 -->
          <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
          
          <form class="realname-form" @submit.prevent="handleRealname">
            <div class="form-group">
              <label class="form-label">真实姓名</label>
              <input 
                type="text"
                class="form-input-simple"
                placeholder="请输入真实姓名"
                v-model="realname"
              />
            </div>
            
            <div class="form-group">
              <label class="form-label">身份证号</label>
              <input 
                type="text"
                class="form-input-simple"
                placeholder="请输入身份证号"
                v-model="idcard"
                maxlength="18"
              />
            </div>
            
            <!-- 认证说明 -->
            <div class="benefit-card">
              <div class="benefit-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
                </svg>
                <span>实名认证后您将获得：</span>
              </div>
              <div class="benefit-list">
                <div class="benefit-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21.801 10A10 10 0 1 1 17 3.335"></path>
                    <path d="m9 11 3 3L22 4"></path>
                  </svg>
                  <span>专属陵水好房码</span>
                </div>
                <div class="benefit-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21.801 10A10 10 0 1 1 17 3.335"></path>
                    <path d="m9 11 3 3L22 4"></path>
                  </svg>
                  <span>隐私保护无骚扰</span>
                </div>
                <div class="benefit-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21.801 10A10 10 0 1 1 17 3.335"></path>
                    <path d="m9 11 3 3L22 4"></path>
                  </svg>
                  <span>购房补贴资格</span>
                </div>
              </div>
            </div>
            
            <button 
              type="submit"
              class="submit-btn"
              :class="{ loading: loading }"
              :disabled="loading"
            >
              <span v-if="loading" class="loading-spinner"></span>
              <span>完成认证</span>
            </button>
          </form>
          
          <p class="privacy-notice">
            您的个人信息将被严格加密保护，仅用于实名认证
          </p>
          
          <div class="security-badges">
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
              </svg>
              <span>信息加密</span>
            </div>
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
              <span>隐私保护</span>
            </div>
            <div class="badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21.801 10A10 10 0 1 1 17 3.335"></path>
                <path d="m9 11 3 3L22 4"></path>
              </svg>
              <span>政府监管</span>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 复用通用页脚 -->
    <AppFooter />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import AppHeader from '../components/AppHeader.vue'
import AppFooter from '../components/AppFooter.vue'
import { useAuth } from '../composables/useAuth'

const router = useRouter()
const { 
  sendSmsCode, 
  sendLoginSmsCode,
  registerUser, 
  loginWithPassword,
  loginWithSms,
  verifyIdcard,
  fetchUserInfo,
  isVerified
} = useAuth()

const step = ref(1)
const loginMode = ref('register') // 'register' 或 'password'
const loginType = ref('password') // 'password' 或 'sms'
const phone = ref('')
const code = ref('')
const loginCode = ref('') // 登录用的验证码
const password = ref('')
const passwordTwo = ref('')
const email = ref('')
const realname = ref('')
const idcard = ref('')
const loading = ref(false)
const countdown = ref(0)
const errorMsg = ref('')

// 切换登录模式
const switchToPasswordLogin = () => {
  loginMode.value = 'password'
  errorMsg.value = ''
}

const switchToRegister = () => {
  loginMode.value = 'register'
  errorMsg.value = ''
}

// 发送登录验证码
const sendLoginCode = async () => {
  if (countdown.value > 0) return
  if (!phone.value || !/^1[3-9]\d{9}$/.test(phone.value)) {
    errorMsg.value = '请输入正确的手机号'
    return
  }
  
  loading.value = true
  errorMsg.value = ''
  
  try {
    const result = await sendLoginSmsCode(phone.value)
    if (result.success) {
      countdown.value = 60
      const timer = setInterval(() => {
        countdown.value--
        if (countdown.value <= 0) {
          clearInterval(timer)
        }
      }, 1000)
    } else {
      errorMsg.value = result.message || '发送失败'
    }
  } catch (error) {
    errorMsg.value = error.message || '发送失败'
  } finally {
    loading.value = false
  }
}

// 密码/验证码登录
const handlePasswordLogin = async () => {
  if (!phone.value || !/^1[3-9]\d{9}$/.test(phone.value)) {
    errorMsg.value = '请输入正确的手机号'
    return
  }
  
  if (loginType.value === 'password') {
    if (!password.value) {
      errorMsg.value = '请输入密码'
      return
    }
  } else {
    if (!loginCode.value || loginCode.value.length !== 6) {
      errorMsg.value = '请输入6位验证码'
      return
    }
  }
  
  loading.value = true
  errorMsg.value = ''
  
  try {
    let result
    if (loginType.value === 'password') {
      result = await loginWithPassword(phone.value, password.value)
    } else {
      result = await loginWithSms(phone.value, loginCode.value)
    }
    
    if (result.success) {
      // 检查是否已实名
      if (isVerified.value) {
        router.push('/')
      } else {
        step.value = 3
      }
    } else {
      errorMsg.value = result.message || '登录失败'
    }
  } catch (error) {
    errorMsg.value = error.message || '登录失败'
  } finally {
    loading.value = false
  }
}

// 发送验证码
const sendCode = async () => {
  if (countdown.value > 0) return
  
  loading.value = true
  errorMsg.value = ''
  
  try {
    const result = await sendSmsCode(phone.value)
    if (result.success) {
      countdown.value = 60
      const timer = setInterval(() => {
        countdown.value--
        if (countdown.value <= 0) {
          clearInterval(timer)
        }
      }, 1000)
    } else {
      // 如果手机号已注册，提示用户登录
      if (result.message?.includes('已注册') || result.message?.includes('已存在')) {
        errorMsg.value = '该手机号已注册，请直接登录'
      } else {
        errorMsg.value = result.message || '发送失败'
      }
    }
  } catch (error) {
    errorMsg.value = error.message || '发送失败'
  } finally {
    loading.value = false
  }
}

// 提交手机号，进入验证码步骤
const handleSubmit = async () => {
  // 验证手机号
  if (!phone.value || !/^1[3-9]\d{9}$/.test(phone.value)) {
    errorMsg.value = '请输入正确的手机号'
    return
  }
  errorMsg.value = ''
  // 进入验证码步骤
  step.value = 2
  sendCode()
}

// 验证验证码并注册
const handleVerify = async () => {
  if (!code.value || code.value.length !== 6) {
    errorMsg.value = '请输入6位验证码'
    return
  }
  if (!email.value || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
    errorMsg.value = '请输入正确的邮箱地址'
    return
  }
  if (!password.value || password.value.length < 6) {
    errorMsg.value = '请输入至少6位密码'
    return
  }
  if (password.value !== passwordTwo.value) {
    errorMsg.value = '两次输入的密码不一致'
    return
  }
  
  loading.value = true
  errorMsg.value = ''
  
  try {
    // 调用注册接口
    const result = await registerUser({
      phone: phone.value,
      email: email.value,
      smsCode: code.value,
      password: password.value,
      passwordTwo: passwordTwo.value
    })
    
    if (result.success) {
      // 注册成功后自动登录
      const loginResult = await loginWithPassword(phone.value, password.value)
      if (loginResult.success) {
        // 检查是否已实名认证
        if (isVerified.value) {
          router.push('/')
        } else {
          // 进入实名认证步骤
          step.value = 3
        }
      } else {
        errorMsg.value = loginResult.message || '登录失败'
      }
    } else {
      errorMsg.value = result.message || '注册失败'
    }
  } catch (error) {
    errorMsg.value = error.message || '操作失败，请重试'
  } finally {
    loading.value = false
  }
}

// 提交实名认证
const handleRealname = async () => {
  if (!realname.value) {
    errorMsg.value = '请输入真实姓名'
    return
  }
  if (!idcard.value || idcard.value.length !== 18) {
    errorMsg.value = '请输入正确的18位身份证号'
    return
  }
  
  loading.value = true
  errorMsg.value = ''
  
  try {
    const result = await verifyIdcard(realname.value, idcard.value)
    
    if (result.success) {
      alert('认证成功！')
      router.push('/')
    } else {
      errorMsg.value = result.message || '认证失败'
    }
  } catch (error) {
    errorMsg.value = error.message || '认证失败，请重试'
  } finally {
    loading.value = false
  }
}

// 返回上一步
const goBack = () => {
  step.value = 1
  code.value = ''
  email.value = ''
  password.value = ''
  passwordTwo.value = ''
  errorMsg.value = ''
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(180deg, #eef4ff 0%, #e8f0f8 100%);
}

/* ===== 主体内容 ===== */
.main-content {
  flex: 1;
  padding: 48px 32px;
}

.content-wrapper {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  gap: 64px;
  align-items: flex-start;
}

/* 左侧信息区域 */
.info-section {
  flex: 1;
}

.main-title {
  font-size: 36px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 8px;
}

.main-subtitle {
  font-size: 18px;
  color: #6b7280;
  margin-bottom: 40px;
}

.features {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-bottom: 32px;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.feature-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.feature-icon.blue {
  background: #eff6ff;
  color: #2563eb;
}

.feature-icon.purple {
  background: #faf5ff;
  color: #9333ea;
}

.feature-icon.gray {
  background: #f3f4f6;
  color: #6b7280;
}

.feature-text {
  padding-top: 4px;
}

.feature-title {
  font-size: 18px;
  font-weight: 400;
  color: #111827;
  margin-bottom: 4px;
}

.feature-desc {
  font-size: 14px;
  color: #2563eb;
}

/* 用户等级卡片 */
.level-card {
  background: #ffffff;
  border-radius: 16px;
  padding: 24px;
  border: 1px solid #e5e7eb;
}

.level-title {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 16px;
}

.level-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 8px;
}

.level-item:last-child {
  margin-bottom: 0;
}

.level-item.gold {
  background: #fffbeb;
}

.level-item.silver {
  background: #f9fafb;
}

.level-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.level-item.gold .level-dot {
  background: #f59e0b;
}

.level-item.silver .level-dot {
  background: #9ca3af;
}

.level-name {
  font-size: 14px;
  font-weight: 500;
  color: #111827;
}

.level-desc {
  font-size: 14px;
  color: #6b7280;
  margin-left: auto;
}

/* ===== 右侧登录卡片 ===== */
.login-card,
.verify-card,
.realname-card {
  width: 520px;
  background: #ffffff;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;
}

/* 登录模式切换 */
.mode-tabs {
  display: flex;
  background: #f3f4f6;
  border-radius: 10px;
  padding: 4px;
  margin-bottom: 24px;
}

.mode-tab {
  flex: 1;
  padding: 10px 16px;
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
  background: transparent;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.mode-tab.active {
  color: #2563eb;
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.mode-tab:hover:not(.active) {
  color: #374151;
}

/* 密码/验证码切换 */
.login-type-switch {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
}

.login-type-switch button {
  font-size: 14px;
  color: #6b7280;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 0;
  border-bottom: 2px solid transparent;
}

.login-type-switch button.active {
  color: #2563eb;
  border-bottom-color: #2563eb;
}

/* 验证码输入框 */
.code-input-wrapper {
  display: flex;
  gap: 12px;
}

.code-input {
  flex: 1;
}

.send-code-btn {
  padding: 0 20px;
  height: 49px;
  font-size: 14px;
  color: #2563eb;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  border-radius: 10px;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
}

.send-code-btn:hover:not(:disabled) {
  background: #dbeafe;
}

.send-code-btn:disabled {
  color: #9ca3af;
  background: #f3f4f6;
  border-color: #e5e7eb;
  cursor: not-allowed;
}

.card-header {
  text-align: center;
  margin-bottom: 32px;
}

.card-title {
  font-size: 24px;
  font-weight: 400;
  color: #111827;
  margin-bottom: 8px;
}

.card-subtitle {
  font-size: 16px;
  color: #6b7280;
}

.error-msg {
  background: #fef2f2;
  color: #dc2626;
  padding: 10px 14px;
  border-radius: 8px;
  font-size: 14px;
  margin-bottom: 16px;
  border: 1px solid #fecaca;
}

.login-form {
  margin-bottom: 24px;
}

.form-group {
  margin-bottom: 24px;
}

.form-label {
  display: block;
  font-size: 14px;
  color: #374151;
  margin-bottom: 8px;
}

.input-wrapper {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
}

.form-input {
  width: 100%;
  height: 49px;
  padding: 12px 16px 12px 40px;
  font-size: 16px;
  color: #111827;
  background: #ffffff;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  outline: none;
  transition: all 0.2s ease;
  box-sizing: border-box;
}

.form-input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-input::placeholder {
  color: #9ca3af;
}

/* 简单输入框（无图标） */
.form-input-simple {
  width: 100%;
  height: 49px;
  padding: 12px 16px;
  font-size: 16px;
  color: #111827;
  background: #ffffff;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  outline: none;
  transition: all 0.2s ease;
  box-sizing: border-box;
}

.form-input-simple:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-input-simple::placeholder {
  color: #9ca3af;
}

.submit-btn {
  width: 100%;
  height: 48px;
  font-size: 16px;
  font-weight: 400;
  color: #ffffff;
  background: #2563eb;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: background 0.15s ease;
}

.submit-btn:hover:not(:disabled) {
  background: #1d4ed8;
}

.submit-btn:disabled {
  background: #93c5fd;
  cursor: not-allowed;
}

.loading-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: #ffffff;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.agreement-text {
  text-align: center;
  font-size: 14px;
  color: #6b7280;
  margin-bottom: 32px;
}

.link-btn {
  font-size: 14px;
  font-weight: 500;
  color: #2563eb;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.link-btn:hover {
  text-decoration: underline;
}

.security-badges {
  display: flex;
  justify-content: center;
  gap: 32px;
}

.badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  color: #6b7280;
}

/* ===== 验证码卡片样式 ===== */
.phone-hint {
  font-size: 14px;
  color: #374151;
  margin-bottom: 24px;
}

.verify-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 32px;
}

.verify-input {
  width: 100%;
  height: 56px;
  padding: 16px;
  font-size: 18px;
  text-align: center;
  color: #111827;
  background: #ffffff;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  outline: none;
  transition: all 0.2s ease;
  box-sizing: border-box;
}

.verify-input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.verify-input::placeholder {
  color: #9ca3af;
  font-size: 16px;
}

.resend-btn {
  font-size: 14px;
  color: #2563eb;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px 0;
  text-align: center;
}

.resend-btn:hover:not(.disabled) {
  text-decoration: underline;
}

.resend-btn.disabled {
  color: #6b7280;
  cursor: not-allowed;
}

.back-btn {
  width: 100%;
  height: 48px;
  font-size: 16px;
  font-weight: 400;
  color: #374151;
  background: #ffffff;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
}

.back-btn:hover {
  background: #f9fafb;
  border-color: #9ca3af;
}

.divider {
  height: 1px;
  background: #e5e7eb;
  margin-bottom: 24px;
}

/* ===== 实名认证卡片样式 ===== */
.realname-form {
  margin-bottom: 24px;
}

.benefit-card {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 24px;
}

.benefit-header {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #6b7280;
  font-size: 14px;
  margin-bottom: 12px;
}

.benefit-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-left: 28px;
}

.benefit-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #22c55e;
}

.benefit-item span {
  color: #374151;
}

.privacy-notice {
  text-align: center;
  font-size: 14px;
  color: #2563eb;
  margin-bottom: 24px;
}

/* ===== 响应式 ===== */
@media (max-width: 1100px) {
  .content-wrapper {
    flex-direction: column;
    align-items: center;
  }
  
  .info-section {
    max-width: 520px;
    width: 100%;
  }
  
  .login-card,
  .verify-card,
  .realname-card {
    width: 100%;
    max-width: 520px;
  }
}
</style>
