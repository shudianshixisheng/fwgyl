<template>
  <section class="cta-section">
    <div class="container">
      <h2 class="cta-title">开启您的安心购房之旅</h2>
      <p class="cta-subtitle">热带海岛滨海精致城市 · 创新创业活力城市</p>
      <div class="cta-buttons">
        <router-link to="/login" class="cta-btn primary">立即注册</router-link>
        <button class="cta-btn secondary">浏览房源</button>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.cta-section {
  width: 100%;
  padding: 80px 0;
  background: #f9fafb;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 32px;
  text-align: center;
}

.cta-title {
  font-size: 30px;
  font-weight: 400;
  color: #1f2937;
  line-height: 36px;
  margin-bottom: 16px;
}

.cta-subtitle {
  font-size: 16px;
  color: #6b7280;
  line-height: 24px;
  margin-bottom: 32px;
}

.cta-buttons {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.cta-btn {
  padding: 12px 32px;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
  transition: all 0.15s ease;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
}

.cta-btn.primary {
  background: #2563eb;
  color: #ffffff;
}

.cta-btn.primary:hover {
  background: #1d4ed8;
}

.cta-btn.secondary {
  background: transparent;
  color: #2563eb;
  border: 1px solid #2563eb;
}

.cta-btn.secondary:hover {
  background: #eff6ff;
}
</style>
