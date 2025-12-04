<template>
	<view class="home-container">
		<!-- Header -->
		<view class="header">
			<view class="header-left">
				<view class="logo-icon"></view>
				<text class="header-title">陵水好房</text>
			</view>
			<text class="header-location">陵水黎族自治县</text>
		</view>
		
		<!-- Banner Swiper -->
		<swiper class="banner-swiper" :autoplay="true" :interval="4000" :circular="true" indicator-dots indicator-color="rgba(255,255,255,0.4)" indicator-active-color="#ffffff">
			<swiper-item>
				<view class="banner-item">
					<image class="banner-bg" src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80" mode="aspectFill" />
					<view class="banner-overlay"></view>
					<view class="banner-content">
						<text class="banner-title">一码勿扰 隐私保护</text>
						<text class="banner-desc">扫码看房 · 无需电话 · 精准匹配</text>
					</view>
				</view>
			</swiper-item>
			<swiper-item>
				<view class="banner-item">
					<image class="banner-bg" src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=80" mode="aspectFill" />
					<view class="banner-overlay"></view>
					<view class="banner-content">
						<text class="banner-title">两保两真 诚信交易</text>
						<text class="banner-desc">真实房源 · 真实价格 · 安心购房</text>
					</view>
				</view>
			</swiper-item>
		</swiper>
		
		<!-- Quick Actions -->
		<view class="quick-actions">
			<view class="action-item" @click="goToPage('search')">
				<view class="action-icon-wrapper blue">
					<view class="action-icon search-icon"></view>
				</view>
				<text class="action-text">找房源</text>
			</view>
			<view class="action-item" @click="goToPage('map')">
				<view class="action-icon-wrapper green">
					<view class="action-icon map-icon"></view>
				</view>
				<text class="action-text">地图找房</text>
			</view>
			<view class="action-item" @click="goToPage('deposit')">
				<view class="action-icon-wrapper orange">
					<view class="action-icon deposit-icon"></view>
				</view>
				<text class="action-text">定金托管</text>
			</view>
		</view>
		
		<!-- 两保两真认证卡片 -->
		<view class="cert-card">
			<view class="cert-header">
				<view class="cert-check-icon"></view>
				<text class="cert-title">两保两真认证标准</text>
			</view>
			<view class="cert-grid">
				<view class="cert-item">
					<text class="cert-item-title">✓ 保真实房源</text>
					<text class="cert-item-desc">住建局审核备案</text>
				</view>
				<view class="cert-item">
					<text class="cert-item-title">✓ 保交付质量</text>
					<text class="cert-item-desc">质保金监管</text>
				</view>
				<view class="cert-item">
					<text class="cert-item-title">✓ 真现房</text>
					<text class="cert-item-desc">竣工备案可查</text>
				</view>
				<view class="cert-item">
					<text class="cert-item-title">✓ 真价格</text>
					<text class="cert-item-desc">一口价无套路</text>
				</view>
			</view>
		</view>
		
		<!-- 热门房源 -->
		<view class="house-section">
			<view class="section-header">
				<text class="section-title">热门房源</text>
				<view class="section-more" @click="goToPage('list')">
					<text class="more-text">查看更多</text>
					<text class="more-arrow">›</text>
				</view>
			</view>
			
			<!-- 房源列表 -->
			<view class="house-list">
				<view class="house-card" v-for="(house, index) in houseList" :key="index" @click="goToDetail(house)">
					<view class="house-info">
						<text class="house-name">{{ house.name }}</text>
						<text class="house-area">{{ house.area }}m² · {{ house.rooms }}</text>
						<view class="house-tags">
							<text class="tag tag-blue">两保两真</text>
							<text class="tag tag-green">现房即买即住</text>
						</view>
					</view>
					<view class="house-price">
						<text class="price-num">{{ house.price }}</text>
						<text class="price-unit">元/m²</text>
						<text class="price-total">总价约{{ house.total }}万</text>
					</view>
				</view>
			</view>
		</view>
		
		<!-- 平台保障 -->
		<view class="section guarantee-section">
			<text class="section-title">平台保障</text>
			<view class="guarantee-list">
				<view class="guarantee-item">
					<view class="guarantee-icon icon-safe"></view>
					<view class="guarantee-content">
						<view class="guarantee-title-row">
							<text class="guarantee-title">定金托管 安全可退</text>
							<text class="guarantee-arrow">›</text>
						</view>
						<text class="guarantee-desc">住建局监管账户，24小时无理由退款</text>
					</view>
				</view>
				<view class="guarantee-item">
					<view class="guarantee-icon icon-privacy"></view>
					<view class="guarantee-content">
						<view class="guarantee-title-row">
							<text class="guarantee-title">一码勿扰 隐私保护</text>
							<text class="guarantee-arrow">›</text>
						</view>
						<text class="guarantee-desc">扫码看房，无需提供手机号码</text>
					</view>
				</view>
				<view class="guarantee-item">
					<view class="guarantee-icon icon-gov"></view>
					<view class="guarantee-content">
						<view class="guarantee-title-row">
							<text class="guarantee-title">政府背书 房协运营</text>
							<text class="guarantee-arrow">›</text>
						</view>
						<text class="guarantee-desc">住建局监管，房协线下核查</text>
					</view>
				</view>
			</view>
		</view>
		
		<!-- 底部快捷操作 -->
		<view class="bottom-actions">
			<view class="bottom-action-item" @click="goToPage('complaint')">
				<view class="bottom-icon icon-complaint"></view>
				<text class="bottom-text">投诉/咨询</text>
			</view>
			<view class="bottom-action-item" @click="goToPage('deposit')">
				<view class="bottom-icon icon-deposit"></view>
				<text class="bottom-text">定金托管</text>
			</view>
			<view class="bottom-action-item" @click="goToPage('suggest')">
				<view class="bottom-icon icon-suggest"></view>
				<text class="bottom-text">投诉建议</text>
			</view>
			<view class="bottom-action-item" @click="goToPage('help')">
				<view class="bottom-icon icon-help"></view>
				<text class="bottom-text">帮助中心</text>
			</view>
		</view>
		
		<!-- 底部占位 -->
		<view class="bottom-placeholder"></view>
		
		<!-- TabBar -->
		<view class="tabbar">
			<view class="tabbar-item active">
				<view class="tabbar-icon icon-home-active"></view>
				<text class="tabbar-text active">首页</text>
			</view>
			<view class="tabbar-item" @click="goToPage('findHouse')">
				<view class="tabbar-icon icon-find"></view>
				<text class="tabbar-text">找房</text>
			</view>
			<view class="tabbar-item" @click="goToPage('map')">
				<view class="tabbar-icon icon-map"></view>
				<text class="tabbar-text">地图</text>
			</view>
			<view class="tabbar-item" @click="goToMine">
				<view class="tabbar-icon icon-mine"></view>
				<text class="tabbar-text">我的</text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			houseList: [
				{
					id: 1,
					name: '海棠湾·碧桂园',
					area: 89,
					rooms: '2室2厅',
					price: '18000',
					total: 160
				},
				{
					id: 2,
					name: '清水湾·雅居乐',
					area: 105,
					rooms: '2室2厅',
					price: '21000',
					total: 221
				},
				{
					id: 3,
					name: '香水湾·融创',
					area: 78,
					rooms: '2室2厅',
					price: '16500',
					total: 129
				}
			]
		}
	},
	methods: {
		goToPage(page) {
			uni.showToast({
				title: '功能开发中',
				icon: 'none'
			});
		},
		goToDetail(house) {
			uni.showToast({
				title: `查看: ${house.name}`,
				icon: 'none'
			});
		},
		goToMine() {
			uni.navigateTo({
				url: '/pages/mine/mine'
			});
		}
	}
}
</script>

<style scoped>
.home-container {
	min-height: 100vh;
	background-color: #f5f7fa;
	padding-bottom: 120rpx;
}

/* Header */
.header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 24rpx 32rpx;
	padding-top: calc(var(--status-bar-height) + 24rpx);
	background-color: #ffffff;
}

.header-left {
	display: flex;
	align-items: center;
	gap: 12rpx;
}

.logo-icon {
	width: 44rpx;
	height: 44rpx;
	background-color: #22c55e;
	border-radius: 10rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2.5'%3E%3Cpath d='M3 21h18'/%3E%3Cpath d='M5 21V7l8-4 8 4v14'/%3E%3Cpath d='M9 21v-4h6v4'/%3E%3C/svg%3E");
	background-size: 26rpx 26rpx;
	background-repeat: no-repeat;
	background-position: center;
}

.header-title {
	font-size: 34rpx;
	color: #2563eb;
	font-weight: 600;
}

.header-location {
	font-size: 28rpx;
	color: #1e3a8a;
}

/* Banner */
.banner-swiper {
	height: 340rpx;
}

.banner-item {
	position: relative;
	height: 100%;
}

.banner-bg {
	width: 100%;
	height: 100%;
}

.banner-overlay {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background: linear-gradient(to bottom, rgba(37, 99, 235, 0.5) 0%, rgba(37, 99, 235, 0.3) 100%);
}

.banner-content {
	position: absolute;
	bottom: 60rpx;
	left: 32rpx;
}

.banner-title {
	display: block;
	font-size: 40rpx;
	color: #ffffff;
	font-weight: 600;
	margin-bottom: 8rpx;
}

.banner-desc {
	font-size: 26rpx;
	color: rgba(255, 255, 255, 0.9);
}

/* Quick Actions */
.quick-actions {
	display: flex;
	justify-content: space-around;
	padding: 48rpx 24rpx;
	background-color: #ffffff;
	margin-bottom: 16rpx;
}

.action-item {
	display: flex;
	flex-direction: column;
	align-items: center;
}

.action-icon-wrapper {
	width: 110rpx;
	height: 110rpx;
	border-radius: 50%;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-bottom: 16rpx;
	border: 2rpx solid;
}

.action-icon-wrapper.blue { 
	background-color: #ffffff; 
	border-color: #dbeafe;
}
.action-icon-wrapper.green { 
	background-color: #ffffff; 
	border-color: #dcfce7;
}
.action-icon-wrapper.orange { 
	background-color: #ffffff; 
	border-color: #fed7aa;
}

.action-icon {
	width: 48rpx;
	height: 48rpx;
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.search-icon {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%232563eb' stroke-width='2'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cpath d='m21 21-4.3-4.3'/%3E%3C/svg%3E");
}

.map-icon {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2322c55e' stroke-width='2'%3E%3Cpath d='M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z'/%3E%3Ccircle cx='12' cy='10' r='3'/%3E%3C/svg%3E");
}

.deposit-icon {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23f97316' stroke-width='2'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cpath d='M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8'/%3E%3Cpath d='M12 18V6'/%3E%3C/svg%3E");
}

.action-text {
	font-size: 26rpx;
	color: #374151;
}

/* Cert Card */
.cert-card {
	margin: 0 24rpx 20rpx;
	background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
	border-radius: 20rpx;
	padding: 32rpx;
}

.cert-header {
	display: flex;
	align-items: center;
	gap: 16rpx;
	margin-bottom: 24rpx;
}

.cert-check-icon {
	width: 40rpx;
	height: 40rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2.5'%3E%3Cpath d='M9 11l3 3L22 4'/%3E%3Cpath d='M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11'/%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
}

.cert-title {
	font-size: 32rpx;
	color: #ffffff;
	font-weight: 600;
}

.cert-grid {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 20rpx;
}

.cert-item {
	background-color: rgba(255, 255, 255, 0.15);
	border-radius: 12rpx;
	padding: 20rpx;
}

.cert-item-title {
	display: block;
	font-size: 28rpx;
	color: #ffffff;
	font-weight: 500;
	margin-bottom: 6rpx;
}

.cert-item-desc {
	font-size: 22rpx;
	color: rgba(255, 255, 255, 0.8);
}

/* Section */
.section {
	background-color: #ffffff;
	margin-bottom: 20rpx;
	padding: 32rpx;
}

.house-section {
	padding: 32rpx;
	background-color: transparent;
}

.section-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 24rpx;
}

.section-title {
	font-size: 36rpx;
	color: #1f2937;
	font-weight: 600;
}

.section-more {
	display: flex;
	align-items: center;
}

.more-text {
	font-size: 26rpx;
	color: #3b82f6;
}

.more-arrow {
	font-size: 32rpx;
	color: #3b82f6;
	margin-left: 4rpx;
}

/* House List */
.house-list {
	display: flex;
	flex-direction: column;
	gap: 24rpx;
}

.house-card {
	display: flex;
	justify-content: space-between;
	padding: 28rpx 24rpx;
	border: 2rpx solid #e5e7eb;
	border-radius: 16rpx;
	background-color: #ffffff;
}

.house-info {
	flex: 1;
}

.house-name {
	display: block;
	font-size: 32rpx;
	color: #1f2937;
	font-weight: 500;
	margin-bottom: 8rpx;
}

.house-area {
	display: block;
	font-size: 26rpx;
	color: #6b7280;
	margin-bottom: 16rpx;
}

.house-tags {
	display: flex;
	gap: 12rpx;
}

.tag {
	font-size: 22rpx;
	padding: 8rpx 16rpx;
	border-radius: 6rpx;
	border: 1rpx solid;
}

.tag-blue {
	color: #2563eb;
	background-color: #eff6ff;
	border-color: #bfdbfe;
}

.tag-green {
	color: #16a34a;
	background-color: #ffffff;
	border-color: #16a34a;
}

.house-price {
	text-align: right;
}

.price-num {
	font-size: 38rpx;
	color: #3b82f6;
	font-weight: 600;
}

.price-unit {
	font-size: 24rpx;
	color: #3b82f6;
}

.price-total {
	display: block;
	font-size: 24rpx;
	color: #9ca3af;
	margin-top: 8rpx;
}

/* Guarantee */
.guarantee-section {
	padding-top: 32rpx;
	margin-top: 0;
}

.guarantee-list {
	display: flex;
	flex-direction: column;
	gap: 24rpx;
}

.guarantee-item {
	display: flex;
	align-items: flex-start;
	gap: 24rpx;
}

.guarantee-icon {
	width: 72rpx;
	height: 72rpx;
	border-radius: 16rpx;
	background-size: 36rpx 36rpx;
	background-repeat: no-repeat;
	background-position: center;
	flex-shrink: 0;
}

.icon-safe {
	background-color: #eff6ff;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%232563eb' stroke-width='2'%3E%3Crect width='18' height='11' x='3' y='11' rx='2' ry='2'/%3E%3Cpath d='M7 11V7a5 5 0 0 1 10 0v4'/%3E%3C/svg%3E");
}

.icon-privacy {
	background-color: #f0fdf4;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2322c55e' stroke-width='2'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10'/%3E%3Cpath d='m9 12 2 2 4-4'/%3E%3C/svg%3E");
}

.icon-gov {
	background-color: #fef3c7;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23f59e0b' stroke-width='2'%3E%3Cpath d='M2 20h20'/%3E%3Cpath d='M5 20V8.5L12 4l7 4.5V20'/%3E%3Cpath d='M9 20v-4h6v4'/%3E%3Cpath d='M9 12h6'/%3E%3Cpath d='M9 8h6'/%3E%3C/svg%3E");
}

.guarantee-content {
	flex: 1;
}

.guarantee-title-row {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 6rpx;
}

.guarantee-title {
	font-size: 30rpx;
	color: #1f2937;
	font-weight: 500;
}

.guarantee-arrow {
	font-size: 32rpx;
	color: #9ca3af;
}

.guarantee-desc {
	font-size: 24rpx;
	color: #6b7280;
}

/* Bottom Actions */
.bottom-actions {
	display: flex;
	justify-content: space-around;
	padding: 32rpx;
	background-color: #ffffff;
	margin-bottom: 20rpx;
}

.bottom-action-item {
	display: flex;
	flex-direction: column;
	align-items: center;
}

.bottom-icon {
	width: 72rpx;
	height: 72rpx;
	border-radius: 50%;
	margin-bottom: 12rpx;
	background-size: 32rpx 32rpx;
	background-repeat: no-repeat;
	background-position: center;
}

.icon-complaint {
	background-color: #fce7f3;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23ec4899' stroke-width='2'%3E%3Cpath d='M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z'/%3E%3C/svg%3E");
}

.icon-deposit {
	background-color: #ccfbf1;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2314b8a6' stroke-width='2'%3E%3Crect width='18' height='11' x='3' y='11' rx='2' ry='2'/%3E%3Cpath d='M7 11V7a5 5 0 0 1 10 0v4'/%3E%3C/svg%3E");
}

.icon-suggest {
	background-color: #dcfce7;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2322c55e' stroke-width='2'%3E%3Cpath d='M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z'/%3E%3Cpath d='M8 10h.01'/%3E%3Cpath d='M12 10h.01'/%3E%3Cpath d='M16 10h.01'/%3E%3C/svg%3E");
}

.icon-help {
	background-color: #ede9fe;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%238b5cf6' stroke-width='2'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cpath d='M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3'/%3E%3Cpath d='M12 17h.01'/%3E%3C/svg%3E");
}

.bottom-text {
	font-size: 22rpx;
	color: #6b7280;
	text-align: center;
}

.bottom-placeholder {
	height: 120rpx;
}

/* TabBar */
.tabbar {
	position: fixed;
	bottom: 0;
	left: 0;
	right: 0;
	display: flex;
	justify-content: space-around;
	align-items: center;
	height: 110rpx;
	background-color: #ffffff;
	border-top: 1rpx solid #f3f4f6;
	padding-bottom: env(safe-area-inset-bottom);
}

.tabbar-item {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 10rpx 0;
}

.tabbar-icon {
	width: 48rpx;
	height: 48rpx;
	margin-bottom: 6rpx;
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.icon-home-active {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='%232563eb' stroke='%232563eb' stroke-width='2'%3E%3Cpath d='m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/%3E%3Cpolyline points='9 22 9 12 15 12 15 22'/%3E%3C/svg%3E");
}

.icon-find {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Crect width='16' height='20' x='4' y='2' rx='2' ry='2'/%3E%3Cpath d='M9 22v-4h6v4'/%3E%3Cpath d='M8 6h.01'/%3E%3Cpath d='M16 6h.01'/%3E%3Cpath d='M12 6h.01'/%3E%3Cpath d='M12 10h.01'/%3E%3Cpath d='M12 14h.01'/%3E%3Cpath d='M16 10h.01'/%3E%3Cpath d='M16 14h.01'/%3E%3Cpath d='M8 10h.01'/%3E%3Cpath d='M8 14h.01'/%3E%3C/svg%3E");
}

.icon-map {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpolygon points='3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21'/%3E%3Cline x1='9' x2='9' y1='3' y2='18'/%3E%3Cline x1='15' x2='15' y1='6' y2='21'/%3E%3C/svg%3E");
}

.icon-mine {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpath d='M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2'/%3E%3Ccircle cx='12' cy='7' r='4'/%3E%3C/svg%3E");
}

.tabbar-text {
	font-size: 22rpx;
	color: #9ca3af;
}

.tabbar-text.active {
	color: #2563eb;
}
</style>
