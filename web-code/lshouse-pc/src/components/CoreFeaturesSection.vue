<template>
  <section class="core-features">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">三大核心功能</h2>
        <p class="section-subtitle">政府信用背书 + 数字化工具赋能 + 市场化规则约束</p>
      </div>
      
      <div class="features-grid">
        <!-- 两保两真 -->
        <div class="feature-card">
          <div class="feature-icon blue">
            <!-- Shield icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
            </svg>
          </div>
          <h3 class="feature-title">两保两真</h3>
          <p class="feature-desc">保真实房源/保交付质量</p>
          <p class="feature-desc-sub">真现房/真价格</p>
        </div>
        
        <!-- 一码勿扰 -->
        <div class="feature-card">
          <div class="feature-icon green">
            <!-- QR Code icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
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
          <h3 class="feature-title">一码勿扰</h3>
          <p class="feature-desc">隐私保护/精准匹配</p>
          <p class="feature-desc-sub">企业微信专属沟通</p>
        </div>
        
        <!-- 定金托管 -->
        <div class="feature-card">
          <div class="feature-icon purple">
            <!-- Lock icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
          </div>
          <h3 class="feature-title">定金托管</h3>
          <p class="feature-desc">安全可退/24小时原路返还</p>
          <p class="feature-desc-sub">住建局/房协监管</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.core-features {
  width: 100%;
  padding: 64px 0;
  background: #ffffff;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 32px;
}

.section-header {
  text-align: center;
  margin-bottom: 48px;
}

.section-title {
  font-size: 30px;
  font-weight: 400;
  color: #1f2937;
  line-height: 36px;
  margin-bottom: 16px;
}

.section-subtitle {
  font-size: 16px;
  color: #6b7280;
  line-height: 24px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.feature-card {
  padding: 32px;
  background: linear-gradient(to bottom right, #f9fafb, #ffffff);
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  transition: box-shadow 0.2s ease;
}

.feature-card:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 24px;
}

.feature-icon.blue {
  background: #dbeafe;
  color: #2563eb;
}

.feature-icon.green {
  background: #d1fae5;
  color: #059669;
}

.feature-icon.purple {
  background: #ede9fe;
  color: #7c3aed;
}

.feature-title {
  font-size: 20px;
  font-weight: 400;
  color: #1f2937;
  line-height: 28px;
  margin-bottom: 8px;
}

.feature-desc {
  font-size: 16px;
  color: #6b7280;
  line-height: 24px;
  margin-bottom: 8px;
}

.feature-desc-sub {
  font-size: 14px;
  color: #9ca3af;
  line-height: 20px;
}
</style>
