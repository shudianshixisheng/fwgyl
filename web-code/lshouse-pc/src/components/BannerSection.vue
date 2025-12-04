<template>
  <section class="banner">
    <div class="banner-slider">
      <!-- 轮播内容 -->
      <div 
        class="banner-slide" 
        v-for="(slide, index) in slides" 
        :key="index"
        :class="{ active: currentSlide === index }"
      >
        <img :src="slide.image" :alt="slide.title" class="slide-bg" />
        <div class="slide-overlay"></div>
        <div class="slide-content">
          <span class="slide-tag">{{ slide.tag }}</span>
          <h1 class="slide-title">{{ slide.title }}</h1>
          <p class="slide-subtitle">{{ slide.subtitle }}</p>
          <button class="slide-btn">
            <span>{{ slide.btnText }}</span>
            <!-- ChevronRight icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="m9 18 6-6-6-6"></path>
            </svg>
          </button>
        </div>
      </div>
      
      <!-- 左箭头 -->
      <button class="arrow arrow-left" @click="prevSlide">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="m15 18-6-6 6-6"></path>
        </svg>
      </button>
      
      <!-- 右箭头 -->
      <button class="arrow arrow-right" @click="nextSlide">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="m9 18 6-6-6-6"></path>
        </svg>
      </button>
      
      <!-- 指示器 - 右下角 -->
      <div class="indicators">
        <button 
          v-for="(_, index) in slides" 
          :key="index"
          class="indicator"
          :class="{ active: currentSlide === index }"
          @click="goToSlide(index)"
        ></button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const currentSlide = ref(0)
let autoplayTimer = null

const slides = [
  {
    tag: '房源推广',
    title: '陵水好房码 · 极速现房交易',
    subtitle: '两保两真 · 一码勿扰 · 定金托管',
    btnText: '立即查看房源',
    image: 'https://images.unsplash.com/photo-1558117338-aa433feb1c62?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  },
  {
    tag: '房源推广',
    title: '100套白名单房源',
    subtitle: '政府信用背书 · 真实房源保障',
    btnText: '立即查看房源',
    image: 'https://images.unsplash.com/photo-1594873604892-b599f847e859?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  },
  {
    tag: '房源推广',
    title: '购房补贴直抵首付',
    subtitle: '岛外客户 · 人才群体专享优惠',
    btnText: '查看补贴政策',
    image: 'https://images.unsplash.com/photo-1623051786509-57224cdc43e1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  },
  {
    tag: '产业发展',
    title: '陵水产业发展 · 黎安国际教育创新试验区',
    subtitle: '国际教育 · 科技创新 · 热带特色农业 · 文旅融合',
    btnText: '了解更多',
    image: 'https://images.unsplash.com/photo-1666243035395-9b7853cecc05?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  },
  {
    tag: '政策支持',
    title: '海南自贸港优惠政策',
    subtitle: '购房补贴 · 人才引进 · 税收优惠 · 落户便利',
    btnText: '查看政策详情',
    image: 'https://images.unsplash.com/photo-1716796484009-b4540dd3ab6a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  },
  {
    tag: '旅游推荐',
    title: '陵水旅游 · 热带滨海度假胜地',
    subtitle: '清水湾 · 分界洲岛 · 南湾猴岛 · 椰子岛',
    btnText: '探索周边房源',
    image: 'https://images.unsplash.com/photo-1631535152690-ba1a85229136?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  },
  {
    tag: '人文介绍',
    title: '陵水人文 · 黎族文化传承',
    subtitle: '非遗文化 · 黎锦技艺 · 民俗风情 · 历史古迹',
    btnText: '了解更多',
    image: 'https://images.unsplash.com/photo-1761677671115-3c6c15d2ed0e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  },
  {
    tag: '美食推荐',
    title: '陵水美食 · 地道海南风味',
    subtitle: '陵水酸粉 · 疍家海鲜 · 椰子饭 · 清补凉',
    btnText: '了解更多',
    image: 'https://images.unsplash.com/photo-1755742319537-449f661a3190?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920'
  }
]

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.length
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + slides.length) % slides.length
}

const goToSlide = (index) => {
  currentSlide.value = index
}

const startAutoplay = () => {
  autoplayTimer = setInterval(() => {
    nextSlide()
  }, 5000)
}

const stopAutoplay = () => {
  if (autoplayTimer) {
    clearInterval(autoplayTimer)
  }
}

onMounted(() => {
  startAutoplay()
})

onUnmounted(() => {
  stopAutoplay()
})
</script>

<style scoped>
.banner {
  width: 100%;
  height: calc((100vh - 64px) * 0.75);
  min-height: 400px;
  max-height: 600px;
  position: relative;
  overflow: hidden;
}

.banner-slider {
  width: 100%;
  height: 100%;
  position: relative;
}

.banner-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.banner-slide.active {
  opacity: 1;
}

.slide-bg {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.slide-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.2) 40%, rgba(0,0,0,0.1) 100%);
}

.slide-content {
  position: absolute;
  top: 50%;
  left: 80px;
  transform: translateY(-50%);
  max-width: 800px;
  z-index: 2;
}

.slide-tag {
  display: inline-block;
  padding: 6px 16px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(4px);
  border-radius: 9999px;
  font-size: 14px;
  color: #ffffff;
  line-height: 20px;
  margin-bottom: 20px;
}

.slide-title {
  font-size: 56px;
  font-weight: 500;
  color: #ffffff;
  line-height: 1.15;
  margin-bottom: 20px;
  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.slide-subtitle {
  font-size: 22px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.9);
  line-height: 32px;
  margin-bottom: 40px;
}

.slide-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 36px;
  background: #2563eb;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 500;
  color: #ffffff;
  line-height: 24px;
  transition: background 0.15s ease;
}

.slide-btn:hover {
  background: #1d4ed8;
}

/* 箭头按钮 */
.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 56px;
  height: 56px;
  background: rgba(107, 114, 128, 0.5);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  color: #ffffff;
  transition: all 0.15s ease;
}

.arrow:hover {
  background: rgba(107, 114, 128, 0.7);
}

.arrow:hover svg {
  transform: scale(1.1);
}

.arrow svg {
  transition: transform 0.15s ease;
}

.arrow-left {
  left: 0;
  border-radius: 0 50% 50% 0;
  padding-left: 8px;
}

.arrow-right {
  right: 0;
  border-radius: 50% 0 0 50%;
  padding-right: 8px;
}

/* 指示器 - 居中 */
.indicators {
  position: absolute;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  z-index: 10;
}

.indicator {
  width: 10px;
  height: 10px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  transition: all 0.2s ease;
}

.indicator:hover {
  background: rgba(255, 255, 255, 0.7);
}

.indicator.active {
  width: 32px;
  background: #ffffff;
  border-radius: 5px;
}
</style>
