<template>
  <section class="process-section">
    <div class="container">
      <div class="process-wrapper">
        <div class="process-grid">
          <!-- 购房流程 -->
          <div class="process-column">
            <h3 class="column-title">购房流程</h3>
            <div class="process-list">
              <div class="process-item" v-for="(step, index) in processSteps" :key="index">
                <div class="step-number">{{ index + 1 }}</div>
                <span class="step-text">{{ step }}</span>
              </div>
            </div>
          </div>
          
          <!-- 应用场景 -->
          <div class="scenario-column">
            <h3 class="column-title">应用场景</h3>
            <div class="scenario-list">
              <div class="scenario-item" v-for="(scenario, index) in scenarios" :key="index">
                <!-- ChevronRight icon -->
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="scenario-icon">
                  <path d="m9 18 6-6-6-6"></path>
                </svg>
                <span class="scenario-label">{{ scenario.label }}：</span>
                <span class="scenario-desc">{{ scenario.desc }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const processSteps = [
  '注册生成"陵水好房码"',
  '浏览白名单认证房源',
  '企业微信无骚扰沟通',
  '定金托管安全交易',
  '申领购房补贴',
  '完成现房交付'
]

const scenarios = [
  { label: '融媒体引流', desc: '抖音/小红书推广' },
  { label: '无骚扰询价', desc: '企业微信专属沟通' },
  { label: '合规销售', desc: '白名单房源真实可售' },
  { label: '定金退还', desc: '24小时原路返还' },
  { label: '补贴申领', desc: '直接抵扣首付' },
  { label: '收益分配', desc: '平台运营/购房补贴/推广' }
]
</script>

<style scoped>
.process-section {
  width: 100%;
  padding: 0 0 64px;
  background: #f9fafb;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 32px;
}

.process-wrapper {
  background: #ffffff;
  border-radius: 14px;
  padding: 32px;
  margin-top: 48px;
}

.process-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}

.column-title {
  font-size: 20px;
  font-weight: 400;
  color: #1f2937;
  line-height: 28px;
  margin-bottom: 16px;
}

.process-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.process-item {
  display: flex;
  align-items: center;
  gap: 12px;
}

.step-number {
  width: 24px;
  height: 24px;
  background: #2563eb;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 500;
  color: #ffffff;
  flex-shrink: 0;
}

.step-text {
  font-size: 14px;
  color: #374151;
  line-height: 20px;
}

.scenario-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.scenario-item {
  display: flex;
  align-items: flex-start;
  gap: 4px;
}

.scenario-icon {
  flex-shrink: 0;
  color: #2563eb;
  margin-top: 0px;
}

.scenario-label {
  font-size: 14px;
  font-weight: 500;
  color: #374151;
  line-height: 20px;
  white-space: nowrap;
}

.scenario-desc {
  font-size: 14px;
  color: #6b7280;
  line-height: 20px;
}
</style>
