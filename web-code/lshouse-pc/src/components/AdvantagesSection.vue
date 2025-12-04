<template>
  <section class="advantages-section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">平台优势</h2>
        <p class="section-subtitle">海南自贸港现房交易标杆</p>
      </div>
      
      <div class="advantages-grid">
        <!-- 住建局审核认证 -->
        <div class="advantage-card">
          <!-- CircleCheckBig icon -->
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="advantage-icon">
            <path d="M21.801 10A10 10 0 1 1 17 3.335"></path>
            <path d="m9 11 3 3L22 4"></path>
          </svg>
          <span class="advantage-text">住建局审核认证</span>
        </div>
        
        <!-- 房协线下核查 -->
        <div class="advantage-card">
          <!-- Award icon -->
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="advantage-icon">
            <path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"></path>
            <circle cx="12" cy="8" r="6"></circle>
          </svg>
          <span class="advantage-text">房协线下核查</span>
        </div>
        
        <!-- VR实景看房 -->
        <div class="advantage-card">
          <!-- Star icon -->
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="advantage-icon">
            <path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path>
          </svg>
          <span class="advantage-text">VR实景看房</span>
        </div>
        
        <!-- 精准地图定位 -->
        <div class="advantage-card">
          <!-- MapPin icon -->
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="advantage-icon">
            <path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path>
            <circle cx="12" cy="10" r="3"></circle>
          </svg>
          <span class="advantage-text">精准地图定位</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.advantages-section {
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
  margin-bottom: 40px;
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

.advantages-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.advantage-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 24px;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  transition: all 0.15s ease;
}

.advantage-card:hover {
  border-color: #2563eb;
  box-shadow: 0 2px 8px rgba(37, 99, 235, 0.1);
}

.advantage-icon {
  flex-shrink: 0;
  color: #2563eb;
}

.advantage-text {
  font-size: 16px;
  font-weight: 400;
  color: #1f2937;
  line-height: 24px;
}
</style>
