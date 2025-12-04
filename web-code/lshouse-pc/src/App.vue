<template>
  <div class="app">
    <router-view />
  </div>
</template>

<script setup>
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  width: 100%;
  min-width: 1280px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #0f172a;
  background: #f9fafb;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.app {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f9fafb;
}

main {
  flex: 1;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  outline: none;
  background: none;
}

ul, ol {
  list-style: none;
}

img {
  max-width: 100%;
  display: block;
}
</style>
