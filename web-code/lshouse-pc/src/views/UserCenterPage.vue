<template>
  <div class="page">
    <AppHeader />
    
    <!-- 蓝色用户横幅 - 全宽 -->
    <div class="user-banner">
      <div class="banner-inner">
        <div class="user-left">
          <img class="avatar" :src="userInfo?.avatar || 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop&crop=face'" />
          <div class="user-text">
            <div class="user-name">{{ displayName }}</div>
            <div class="user-meta">{{ maskedPhone }} &nbsp;&nbsp;•&nbsp;&nbsp; 注册于 {{ registerDate }}</div>
          </div>
        </div>
        <div class="user-right">
          <div class="badge-gold"><span class="badge-dot"></span>{{ userLevelText || '金码用户' }}</div>
          <div class="badge-credit">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            信用分：{{ creditScore }}
          </div>
        </div>
      </div>
    </div>

    <div class="content-wrap">
      <!-- 好房码区域 - 一个大白色背景 -->
      <div class="qr-section">
        <div class="qr-left">
          <div class="qr-icon-wrap">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect width="5" height="5" x="3" y="3" rx="1"/><rect width="5" height="5" x="16" y="3" rx="1"/><rect width="5" height="5" x="3" y="16" rx="1"/><path d="M21 16h-3a2 2 0 0 0-2 2v3M21 21v.01M12 7v3a2 2 0 0 1-2 2H7M3 12h.01M12 3h.01M12 16v.01M16 12h1M21 12v.01M12 21v-1"/></svg>
          </div>
          <div class="qr-content">
            <div class="qr-title">我的好房码</div>
            <div class="qr-desc">扫码即可无骚扰看房</div>
            <div class="qr-btns">
              <button class="btn-primary">查看二维码</button>
              <button class="btn-outline">分享好房码</button>
            </div>
          </div>
        </div>
        <div class="stat-cards">
          <div class="stat-card purple">
            <div class="stat-num">3</div>
            <div class="stat-label">收藏房源</div>
          </div>
          <div class="stat-card blue">
            <div class="stat-num">1</div>
            <div class="stat-label">定金订单</div>
          </div>
          <div class="stat-card green">
            <div class="stat-num">16</div>
            <div class="stat-label">累计补贴(万)</div>
          </div>
        </div>
      </div>

      <!-- 主面板 -->
      <div class="main-panel">
        <!-- Tabs -->
        <div class="tabs-bar">
          <div class="tab active">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            个人信息
          </div>
          <div class="tab">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
            收藏房源
          </div>
          <div class="tab">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            定金管理
          </div>
          <div class="tab">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8M16 17H8"/></svg>
            补贴申请
          </div>
        </div>

        <!-- 表单内容 -->
        <div class="panel-content">
          <div class="form-grid">
            <div class="form-field">
              <div class="field-label">真实姓名</div>
              <div class="field-value">{{ verifyInfo?.idcard_name || '未实名' }}</div>
            </div>
            <div class="form-field">
              <div class="field-label">手机号</div>
              <div class="field-value">{{ maskedPhone }}</div>
            </div>
            <div class="form-field">
              <div class="field-label">身份证号</div>
              <div class="field-value">{{ isVerified ? '已认证' : '未认证' }}</div>
            </div>
            <div class="form-field">
              <div class="field-label">信用评分</div>
              <div class="credit-field">
                <span class="credit-score">{{ creditScore }} 分</span>
                <div class="credit-bar"><div class="credit-fill" :style="{ width: (creditScore / 850 * 100) + '%' }"></div></div>
                <span class="credit-tag">{{ creditScore >= 700 ? '优秀' : creditScore >= 600 ? '良好' : '一般' }}</span>
              </div>
            </div>
          </div>

          <!-- 账户设置 -->
          <div class="settings-section">
            <div class="settings-title">账户设置</div>
            <div class="setting-row">
              <div class="setting-left">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/></svg>
                修改个人信息
              </div>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="arrow"><path d="m9 18 6-6-6-6"/></svg>
            </div>
            <div class="setting-row">
              <div class="setting-left">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                隐私设置
              </div>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="arrow"><path d="m9 18 6-6-6-6"/></svg>
            </div>
            <div class="setting-row highlight">
              <div class="setting-left">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg>
                申请购房补贴
              </div>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="arrow"><path d="m9 18 6-6-6-6"/></svg>
            </div>
            <div class="setting-row logout" @click="handleLogout">
              <div class="setting-left">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
                退出登录
              </div>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="arrow"><path d="m9 18 6-6-6-6"/></svg>
            </div>
          </div>
        </div>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import AppHeader from '../components/AppHeader.vue'
import AppFooter from '../components/AppFooter.vue'
import { useAuth } from '../composables/useAuth'

const router = useRouter()
const { 
  userInfo, 
  verifyInfo, 
  isLoggedIn, 
  isVerified,
  userLevelText,
  fetchUserInfo,
  logout 
} = useAuth()

// 计算显示的用户名
const displayName = computed(() => {
  if (verifyInfo.value?.idcard_name) return verifyInfo.value.idcard_name
  if (userInfo.value?.name) return userInfo.value.name
  return '用户'
})

// 隐藏手机号中间4位
const maskedPhone = computed(() => {
  const phone = userInfo.value?.phone || ''
  if (phone.length === 11) {
    return phone.slice(0, 3) + '****' + phone.slice(7)
  }
  return phone
})

// 格式化注册时间
const registerDate = computed(() => {
  const datetime = userInfo.value?.create_datetime
  if (datetime) {
    return datetime.split(' ')[0]
  }
  return ''
})

// 信用分（暂用默认值，待接口提供）
const creditScore = computed(() => 750)

// 页面加载时获取用户信息
onMounted(async () => {
  if (!isLoggedIn.value) {
    router.push('/login')
    return
  }
  await fetchUserInfo()
})

// 退出登录
const handleLogout = () => {
  logout()
  router.push('/login')
}
</script>

<style scoped>
.page {
  min-height: 100vh;
  background: #f5f5f5;
  display: flex;
  flex-direction: column;
}

.content-wrap {
  flex: 1;
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
  padding: 16px 16px 40px;
}

/* 蓝色用户横幅 - 全宽 */
.user-banner {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  padding: 24px 0;
}

.banner-inner {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-left {
  display: flex;
  align-items: center;
  gap: 14px;
}

.avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  object-fit: cover;
}

.user-name {
  font-size: 22px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 2px;
}

.user-meta {
  font-size: 13px;
  color: rgba(255,255,255,0.8);
}

.user-right {
  text-align: right;
}

.badge-gold {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 6px;
  color: #fbbf24;
  font-size: 14px;
  margin-bottom: 6px;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: #fbbf24;
  border-radius: 50%;
}

.badge-credit {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 4px;
  color: rgba(255,255,255,0.9);
  font-size: 13px;
}

/* 好房码区域 - 一个大白色背景 */
.qr-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff;
  border-radius: 12px;
  padding: 20px 24px;
  margin-bottom: 16px;
}

.qr-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.qr-icon-wrap {
  width: 72px;
  height: 72px;
  background: #f3f4f6;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #9ca3af;
  flex-shrink: 0;
}

.qr-title {
  font-size: 15px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 2px;
}

.qr-desc {
  font-size: 12px;
  color: #6b7280;
  margin-bottom: 10px;
}

.qr-btns {
  display: flex;
  gap: 8px;
}

.btn-primary {
  padding: 5px 14px;
  background: #3b82f6;
  color: #fff;
  border: none;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
}

.btn-outline {
  padding: 5px 14px;
  background: #fff;
  color: #374151;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
}

/* 统计卡片 */
.stat-cards {
  display: flex;
  gap: 10px;
}

.stat-card {
  border-radius: 12px;
  padding: 14px 20px;
  text-align: center;
  min-width: 80px;
}

.stat-card.purple {
  background: #f3e8ff;
}

.stat-card.blue {
  background: #e0f2fe;
}

.stat-card.green {
  background: #dcfce7;
}

.stat-card.purple .stat-num { color: #a855f7; }
.stat-card.blue .stat-num { color: #3b82f6; }
.stat-card.green .stat-num { color: #22c55e; }

.stat-num {
  font-size: 24px;
  font-weight: 600;
  line-height: 1.2;
}

.stat-label {
  font-size: 11px;
  color: #6b7280;
  margin-top: 2px;
}

/* 主面板 */
.main-panel {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
}

.tabs-bar {
  display: flex;
  border-bottom: 1px solid #e5e7eb;
  padding: 0 16px;
}

.tab {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 14px 14px;
  font-size: 13px;
  color: #6b7280;
  cursor: pointer;
  position: relative;
}

.tab.active {
  color: #3b82f6;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 14px;
  right: 14px;
  height: 2px;
  background: #3b82f6;
}

.panel-content {
  padding: 20px 24px;
}

/* 表单 */
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 32px;
}

.form-field.full {
  grid-column: span 2;
}

.field-label {
  font-size: 12px;
  color: #6b7280;
  margin-bottom: 8px;
}

.field-value {
  font-size: 14px;
  color: #1f2937;
  background: #f9fafb;
  padding: 12px 16px;
  border-radius: 6px;
}

/* 信用评分 */
.credit-field {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #f9fafb;
  padding: 12px 16px;
  border-radius: 6px;
}

.credit-score {
  font-size: 14px;
  color: #1f2937;
}

.credit-bar {
  flex: 1;
  max-width: 280px;
  height: 8px;
  background: #e5e7eb;
  border-radius: 4px;
}

.credit-fill {
  width: 88%;
  height: 100%;
  background: linear-gradient(90deg, #22c55e, #16a34a);
  border-radius: 3px;
}

.credit-tag {
  font-size: 12px;
  color: #16a34a;
  font-weight: 500;
}

/* 账户设置 */
.settings-section {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #f3f4f6;
}

.settings-title {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 8px;
}

.setting-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background: #f9fafb;
  border-radius: 6px;
  margin-bottom: 8px;
  cursor: pointer;
}

.setting-left {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: #374151;
}

.setting-left svg {
  color: #9ca3af;
}

.arrow {
  color: #d1d5db;
}

/* 高亮行 */
.setting-row.highlight {
  background: #eff6ff;
  margin-bottom: 0;
}

.setting-row.highlight .setting-left {
  color: #2563eb;
}

.setting-row.highlight .setting-left svg {
  color: #2563eb;
}

.setting-row.highlight .arrow {
  color: #2563eb;
}

/* 退出登录 */
.setting-row.logout {
  background: #fef2f2;
  margin-top: 16px;
  margin-bottom: 0;
}

.setting-row.logout .setting-left {
  color: #dc2626;
}

.setting-row.logout .setting-left svg {
  color: #dc2626;
}

.setting-row.logout .arrow {
  color: #dc2626;
}
</style>
