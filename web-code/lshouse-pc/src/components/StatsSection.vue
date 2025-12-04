<template>
  <section class="stats-section">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item" v-for="(stat, index) in stats" :key="index">
          <div class="stat-value">
            <span class="stat-number">{{ stat.number }}</span>
            <span class="stat-unit">{{ stat.unit }}</span>
          </div>
          <div class="stat-label">{{ stat.label }}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const stats = [
  { number: '100+', unit: ' 套', label: '白名单房源' },
  { number: '6000', unit: ' 万元', label: '目标成交额' },
  { number: '90', unit: ' %', label: '用户满意度' },
  { number: '3000+', unit: ' 人', label: '平台日活' }
]
</script>

<style scoped>
.stats-section {
  width: 100%;
  background: #2563eb;
  padding: 48px 0;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
}

.stat-item {
  text-align: center;
}

.stat-value {
  display: flex;
  align-items: baseline;
  justify-content: center;
  margin-bottom: 8px;
}

.stat-number {
  font-size: 44px;
  font-weight: 600;
  color: #ffffff;
  line-height: 1;
  letter-spacing: -1px;
}

.stat-unit {
  font-size: 16px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.85);
  margin-left: 4px;
}

.stat-label {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.75);
  line-height: 20px;
}
</style>
