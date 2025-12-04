<template>
  <header class="header">
    <div class="header-container">
      <div class="header-content">
        <!-- Logo区域 -->
        <router-link to="/" class="logo">
          <div class="logo-icon">
            <!-- Building2 icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 12h4"></path>
              <path d="M10 8h4"></path>
              <path d="M14 21v-3a2 2 0 0 0-4 0v3"></path>
              <path d="M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2"></path>
              <path d="M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"></path>
            </svg>
          </div>
          <div class="logo-text">
            <span class="logo-title">陵水好房码</span>
            <span class="logo-subtitle">极速现房交易平台</span>
          </div>
        </router-link>
        
        <!-- 导航菜单 - 居中 -->
        <nav class="nav">
          <router-link to="/" class="nav-item active">
            <!-- House icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"></path>
              <path d="M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
            </svg>
            <span>首页</span>
          </router-link>
          <button class="nav-item">
            <!-- Building2 icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 12h4"></path>
              <path d="M10 8h4"></path>
              <path d="M14 21v-3a2 2 0 0 0-4 0v3"></path>
              <path d="M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2"></path>
              <path d="M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"></path>
            </svg>
            <span>房源</span>
          </button>
          <button class="nav-item">
            <!-- FileText icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"></path>
              <path d="M14 2v5a1 1 0 0 0 1 1h5"></path>
              <path d="M10 9H8"></path>
              <path d="M16 13H8"></path>
              <path d="M16 17H8"></path>
            </svg>
            <span>政策补贴</span>
          </button>
          <button class="nav-item">
            <!-- Building2 icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 12h4"></path>
              <path d="M10 8h4"></path>
              <path d="M14 21v-3a2 2 0 0 0-4 0v3"></path>
              <path d="M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2"></path>
              <path d="M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"></path>
            </svg>
            <span>企业入驻</span>
          </button>
          <button class="nav-item">
            <!-- MessageSquare icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 17a2 2 0 0 1-2 2H6.828a2 2 0 0 0-1.414.586l-2.202 2.202A.71.71 0 0 1 2 21.286V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z"></path>
            </svg>
            <span>投诉建议</span>
          </button>
        </nav>
        
        <!-- 登录注册按钮 / 用户信息 -->
        <div v-if="!isLoggedIn" class="auth-section">
          <router-link to="/login" class="login-btn">
            <!-- User icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <span>登录/注册</span>
          </router-link>
        </div>
        <div v-else class="auth-section user-section">
          <router-link to="/user-center" class="user-badge" :class="{ gold: userLevel === 'gold', silver: userLevel === 'silver' }">
            <span class="user-dot"></span>
            <span>{{ userLevelText }}</span>
          </router-link>
          <button class="logout-btn" @click="handleLogout">
            <!-- LogOut icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" x2="9" y1="12" y2="12"></line>
            </svg>
            <span>退出</span>
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useAuth } from '../composables/useAuth'
import { useRouter } from 'vue-router'

const { isLoggedIn, userLevel, userLevelText, logout } = useAuth()
const router = useRouter()

const handleLogout = () => {
  if (confirm('确定要退出登录吗？')) {
    logout()
    router.push('/')
  }
}
</script>

<style scoped>
.header {
  width: 100%;
  height: 64px;
  background: #ffffff;
  position: sticky;
  top: 0;
  z-index: 50;
}

.header-container {
  width: 100%;
  height: 100%;
  padding: 0 40px;
}

.header-content {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

/* Logo 区域 */
.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
  margin-left: 100px;
  text-decoration: none;
  cursor: pointer;
}

.logo-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2563eb;
}

.logo-text {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.logo-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
  line-height: 1.3;
}

.logo-subtitle {
  font-size: 11px;
  color: #9ca3af;
  line-height: 1.3;
}

/* 导航菜单 - 靠近Logo */
.nav {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: 40px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: transparent;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 400;
  color: #374151;
  line-height: 24px;
  transition: all 0.15s ease;
  white-space: nowrap;
  text-decoration: none;
  cursor: pointer;
}

.nav-item:hover {
  background: #eff6ff;
  color: #2563eb;
}

.nav-item.active {
  background: #eff6ff;
  color: #2563eb;
}

.nav-item svg {
  flex-shrink: 0;
}

/* 认证区域 */
.auth-section {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
  margin-left: auto;
  margin-right: 100px;
}

/* 登录按钮 */
.login-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 20px;
  background: #2563eb;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 400;
  color: #ffffff;
  line-height: 24px;
  height: 40px;
  transition: background 0.15s ease;
  flex-shrink: 0;
  text-decoration: none;
}

.login-btn:hover {
  background: #1d4ed8;
}

.login-btn svg {
  flex-shrink: 0;
}

/* 用户徽章 */
.user-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 24px;
  font-size: 14px;
  font-weight: 400;
  line-height: 24px;
  height: 40px;
  text-decoration: none;
  cursor: pointer;
  transition: opacity 0.2s;
}

.user-badge:hover {
  opacity: 0.9;
}

.user-badge.gold {
  background: #fef3c7;
  color: #92400e;
}

.user-badge.silver {
  background: #f3f4f6;
  color: #374151;
}

.user-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.user-badge.gold .user-dot {
  background: #f59e0b;
}

.user-badge.silver .user-dot {
  background: #9ca3af;
}

/* 退出按钮 */
.logout-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: transparent;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 400;
  color: #6b7280;
  line-height: 24px;
  height: 40px;
  transition: all 0.15s ease;
  cursor: pointer;
}

.logout-btn:hover {
  background: #f9fafb;
  border-color: #d1d5db;
  color: #374151;
}

.logout-btn svg {
  flex-shrink: 0;
}
</style>
