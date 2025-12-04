<template>
  <div class="home-page">
    <AppHeader />
    <main>
      <BannerSection />
      <CoreFeaturesSection />
      <StatsSection />
      <AdvantagesSection />
      <ProcessSection />
      <CtaSection />
    </main>
    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from '../components/AppHeader.vue'
import BannerSection from '../components/BannerSection.vue'
import CoreFeaturesSection from '../components/CoreFeaturesSection.vue'
import StatsSection from '../components/StatsSection.vue'
import AdvantagesSection from '../components/AdvantagesSection.vue'
import ProcessSection from '../components/ProcessSection.vue'
import CtaSection from '../components/CtaSection.vue'
import AppFooter from '../components/AppFooter.vue'
</script>

<style scoped>
.home-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f9fafb;
}

main {
  flex: 1;
}
</style>

