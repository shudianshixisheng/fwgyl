<template>
	<view class="mine-container">
		<!-- 顶部用户区域 -->
		<view class="user-header">
			<view class="user-info" @click="goToSettings">
				<view class="avatar">
					<view class="avatar-icon"></view>
				</view>
				<view class="user-detail">
					<text class="user-name">{{ userName }}</text>
					<text class="user-phone">{{ maskedPhone }}</text>
				</view>
			</view>
			<view class="user-right" @click="goToSettings">
				<view class="verified-badge" v-if="isVerified">
					<view class="verified-icon"></view>
					<text class="verified-text">已实名</text>
				</view>
				<view class="unverified-badge" v-else>
					<text class="unverified-text">未实名</text>
				</view>
				<text class="arrow">›</text>
			</view>
		</view>
		
		<!-- 陵水好房码卡片 -->
		<view class="code-card">
			<view class="code-header">
				<view class="code-info">
					<text class="code-title">陵水好房码</text>
					<view class="code-meta">
						<view class="gold-badge">金码</view>
						<text class="credit-text">信用分：750</text>
					</view>
				</view>
				<view class="view-code-btn">
					<text class="view-code-text">查看码</text>
				</view>
			</view>
			<view class="code-stats">
				<view class="stat-item">
					<text class="stat-num">2</text>
					<text class="stat-label">关注房源</text>
				</view>
				<view class="stat-item">
					<text class="stat-num">5</text>
					<text class="stat-label">浏览记录</text>
				</view>
				<view class="stat-item">
					<text class="stat-num">1</text>
					<text class="stat-label">托管订单</text>
				</view>
			</view>
		</view>
		
		<!-- 我的订单 -->
		<view class="section">
			<view class="section-header">
				<text class="section-title">我的订单</text>
				<view class="section-more">
					<text class="more-text">查看全部</text>
				</view>
			</view>
			
			<view class="order-list">
				<view class="order-item" v-for="(order, index) in orderList" :key="index">
					<view class="order-info">
						<text class="order-name">{{ order.name }}</text>
						<text class="order-date">{{ order.date }}</text>
						<text class="order-deposit">定金：¥{{ order.deposit }}</text>
					</view>
					<view class="order-right">
						<text class="order-status" :class="order.statusClass">{{ order.status }}</text>
						<text class="order-action" :class="order.actionClass">{{ order.action }}</text>
					</view>
				</view>
			</view>
		</view>
		
		<!-- 我的服务 -->
		<view class="section">
			<text class="section-title">我的服务</text>
			<view class="service-list">
				<view class="service-item" @click="goToPage('complaint')">
					<view class="service-icon icon-complaint"></view>
					<view class="service-content">
						<text class="service-title">投诉/咨询</text>
						<text class="service-desc">提交投诉或咨询问题</text>
					</view>
					<text class="service-arrow">›</text>
				</view>
				<view class="service-item" @click="goToSettings">
					<view class="service-icon icon-settings"></view>
					<view class="service-content">
						<text class="service-title">设置</text>
						<text class="service-desc">账户与实名认证</text>
					</view>
					<text class="service-arrow">›</text>
				</view>
			</view>
		</view>
		
		<!-- 平台保障 -->
		<view class="section guarantee-section">
			<view class="guarantee-header">
				<view class="guarantee-check"></view>
				<text class="section-title">平台保障</text>
			</view>
			<view class="guarantee-list">
				<text class="guarantee-item">• 定金托管，安全可退</text>
				<text class="guarantee-item">• 隐私保护，一码勿扰</text>
				<text class="guarantee-item">• 政府监管，房协运营</text>
			</view>
		</view>
		
		<!-- 客服热线 -->
		<view class="hotline-section">
			<text class="hotline-label">客服热线</text>
			<text class="hotline-number">400-888-8888</text>
		</view>
		
		<!-- 底部占位 -->
		<view class="bottom-placeholder"></view>
		
		<!-- TabBar -->
		<view class="tabbar">
			<view class="tabbar-item" @click="goToHome">
				<view class="tabbar-icon icon-home"></view>
				<text class="tabbar-text">首页</text>
			</view>
			<view class="tabbar-item">
				<view class="tabbar-icon icon-find"></view>
				<text class="tabbar-text">找房</text>
			</view>
			<view class="tabbar-item">
				<view class="tabbar-icon icon-map"></view>
				<text class="tabbar-text">地图</text>
			</view>
			<view class="tabbar-item active">
				<view class="tabbar-icon icon-mine-active"></view>
				<text class="tabbar-text active">我的</text>
			</view>
		</view>
	</view>
</template>

<script>
import { getUserInfo, getVerifyStatus } from '@/utils/api.js';

export default {
	data() {
		return {
			userInfo: null,
			isVerified: false,
			verifyInfo: null,
			orderList: [
				{
					name: '海棠湾·碧桂园',
					date: '2024-11-28',
					deposit: '50,000',
					status: '定金已托管',
					statusClass: 'status-blue',
					action: '申请退款',
					actionClass: 'action-blue'
				},
				{
					name: '清水湾·雅居乐',
					date: '2024-11-15',
					deposit: '50,000',
					status: '已取消',
					statusClass: 'status-gray',
					action: '再次购房',
					actionClass: 'action-default'
				}
			]
		}
	},
	computed: {
		userName() {
			if (this.verifyInfo?.idcard_name) {
				return this.verifyInfo.idcard_name.charAt(0) + '先生';
			}
			if (this.userInfo?.name) {
				return this.userInfo.name;
			}
			return '用户';
		},
		maskedPhone() {
			const phone = this.userInfo?.phone || '';
			if (phone.length === 11) {
				return phone.substring(0, 3) + '****' + phone.substring(7);
			}
			return phone;
		}
	},
	onShow() {
		this.loadUserData();
	},
	methods: {
		async loadUserData() {
			// 先从缓存读取
			const cachedUser = uni.getStorageSync('userInfo');
			if (cachedUser) {
				this.userInfo = cachedUser;
			}
			
			// 获取最新用户信息
			try {
				const res = await getUserInfo();
				this.userInfo = res.data;
				uni.setStorageSync('userInfo', res.data);
			} catch (err) {
				console.log('获取用户信息失败', err);
			}
			
			// 获取实名状态
			try {
				const verifyRes = await getVerifyStatus();
				this.isVerified = verifyRes.data.is_verified;
				this.verifyInfo = verifyRes.data;
			} catch (err) {
				console.log('获取实名状态失败', err);
			}
		},
		goToSettings() {
			uni.navigateTo({
				url: '/pages/settings/settings'
			});
		},
		goToHome() {
			uni.reLaunch({
				url: '/pages/index/index'
			});
		},
		goToPage(page) {
			uni.showToast({
				title: '功能开发中',
				icon: 'none'
			});
		}
	}
}
</script>

<style scoped>
.mine-container {
	min-height: 100vh;
	background-color: #f5f7fa;
	padding-bottom: 120rpx;
}

/* 用户头部 */
.user-header {
	background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
	padding: 48rpx 32rpx;
	padding-top: calc(var(--status-bar-height) + 48rpx);
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.user-info {
	display: flex;
	align-items: center;
	gap: 24rpx;
}

.avatar {
	width: 96rpx;
	height: 96rpx;
	background-color: rgba(255, 255, 255, 0.2);
	border-radius: 50%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.avatar-icon {
	width: 56rpx;
	height: 56rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2'%3E%3Cpath d='M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2'/%3E%3Ccircle cx='12' cy='7' r='4'/%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}

.user-detail {
	display: flex;
	flex-direction: column;
	gap: 8rpx;
}

.user-name {
	font-size: 36rpx;
	color: #ffffff;
	font-weight: 600;
}

.user-phone {
	font-size: 26rpx;
	color: rgba(255, 255, 255, 0.8);
}

.user-right {
	display: flex;
	align-items: center;
	gap: 12rpx;
}

.verified-badge {
	display: flex;
	align-items: center;
	gap: 8rpx;
	background-color: rgba(255, 255, 255, 0.2);
	padding: 8rpx 16rpx;
	border-radius: 100rpx;
}

.verified-icon {
	width: 24rpx;
	height: 24rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2.5'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10'/%3E%3Cpath d='m9 12 2 2 4-4'/%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
}

.verified-text {
	font-size: 24rpx;
	color: #ffffff;
}

.unverified-badge {
	background-color: rgba(255, 255, 255, 0.2);
	padding: 8rpx 16rpx;
	border-radius: 100rpx;
}

.unverified-text {
	font-size: 24rpx;
	color: rgba(255, 255, 255, 0.8);
}

.arrow {
	font-size: 36rpx;
	color: rgba(255, 255, 255, 0.8);
}

/* 好房码卡片 */
.code-card {
	margin: -40rpx 24rpx 24rpx;
	background-color: #ffffff;
	border-radius: 20rpx;
	padding: 32rpx;
	box-shadow: 0 8rpx 32rpx rgba(0, 0, 0, 0.08);
	position: relative;
	z-index: 10;
}

.code-header {
	display: flex;
	justify-content: space-between;
	align-items: flex-start;
	margin-bottom: 32rpx;
}

.code-info {
	display: flex;
	flex-direction: column;
	gap: 12rpx;
}

.code-title {
	font-size: 32rpx;
	color: #1f2937;
	font-weight: 600;
}

.code-meta {
	display: flex;
	align-items: center;
	gap: 16rpx;
}

.gold-badge {
	background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
	color: #ffffff;
	font-size: 22rpx;
	padding: 4rpx 12rpx;
	border-radius: 6rpx;
	font-weight: 500;
}

.credit-text {
	font-size: 26rpx;
	color: #6b7280;
}

.view-code-btn {
	background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
	padding: 16rpx 32rpx;
	border-radius: 8rpx;
}

.view-code-text {
	font-size: 28rpx;
	color: #ffffff;
}

.code-stats {
	display: flex;
	justify-content: space-around;
	border-top: 1rpx solid #f3f4f6;
	padding-top: 24rpx;
}

.stat-item {
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 8rpx;
}

.stat-num {
	font-size: 36rpx;
	color: #1f2937;
	font-weight: 600;
}

.stat-label {
	font-size: 24rpx;
	color: #9ca3af;
}

/* Section */
.section {
	background-color: #ffffff;
	margin-bottom: 20rpx;
	padding: 32rpx;
}

.section-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 24rpx;
}

.section-title {
	font-size: 32rpx;
	color: #1f2937;
	font-weight: 600;
}

.more-text {
	font-size: 26rpx;
	color: #3b82f6;
}

/* 订单列表 */
.order-list {
	display: flex;
	flex-direction: column;
	gap: 24rpx;
}

.order-item {
	display: flex;
	justify-content: space-between;
	padding: 24rpx;
	border: 1rpx solid #f3f4f6;
	border-radius: 12rpx;
}

.order-info {
	display: flex;
	flex-direction: column;
	gap: 8rpx;
}

.order-name {
	font-size: 30rpx;
	color: #1f2937;
	font-weight: 500;
}

.order-date {
	font-size: 24rpx;
	color: #9ca3af;
}

.order-deposit {
	font-size: 26rpx;
	color: #6b7280;
}

.order-right {
	display: flex;
	flex-direction: column;
	align-items: flex-end;
	gap: 16rpx;
}

.order-status {
	font-size: 24rpx;
}

.status-blue {
	color: #3b82f6;
}

.status-gray {
	color: #9ca3af;
}

.order-action {
	font-size: 26rpx;
}

.action-blue {
	color: #3b82f6;
}

.action-default {
	color: #1f2937;
}

/* 服务列表 */
.service-list {
	display: flex;
	flex-direction: column;
	gap: 16rpx;
	margin-top: 24rpx;
}

.service-item {
	display: flex;
	align-items: center;
	gap: 24rpx;
	padding: 20rpx 0;
}

.service-icon {
	width: 72rpx;
	height: 72rpx;
	border-radius: 16rpx;
	background-size: 36rpx 36rpx;
	background-repeat: no-repeat;
	background-position: center;
}

.icon-complaint {
	background-color: #fef3c7;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23f59e0b' stroke-width='2'%3E%3Cpath d='M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z'/%3E%3C/svg%3E");
}

.icon-settings {
	background-color: #f3f4f6;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%236b7280' stroke-width='2'%3E%3Cpath d='M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/svg%3E");
}

.service-content {
	flex: 1;
	display: flex;
	flex-direction: column;
	gap: 6rpx;
}

.service-title {
	font-size: 30rpx;
	color: #1f2937;
}

.service-desc {
	font-size: 24rpx;
	color: #9ca3af;
}

.service-arrow {
	font-size: 32rpx;
	color: #d1d5db;
}

/* 平台保障 */
.guarantee-section {
	padding-top: 24rpx;
}

.guarantee-header {
	display: flex;
	align-items: center;
	gap: 12rpx;
	margin-bottom: 20rpx;
}

.guarantee-check {
	width: 36rpx;
	height: 36rpx;
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='%2322c55e' stroke='%2322c55e' stroke-width='2'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10'/%3E%3Cpath d='m9 12 2 2 4-4' stroke='white'/%3E%3C/svg%3E");
	background-size: contain;
	background-repeat: no-repeat;
}

.guarantee-list {
	display: flex;
	flex-direction: column;
	gap: 12rpx;
}

.guarantee-item {
	font-size: 26rpx;
	color: #6b7280;
	line-height: 1.6;
}

/* 客服热线 */
.hotline-section {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 48rpx 32rpx;
	gap: 12rpx;
}

.hotline-label {
	font-size: 26rpx;
	color: #9ca3af;
}

.hotline-number {
	font-size: 36rpx;
	color: #3b82f6;
	font-weight: 500;
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

.icon-home {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpath d='m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/%3E%3Cpolyline points='9 22 9 12 15 12 15 22'/%3E%3C/svg%3E");
}

.icon-find {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Crect width='16' height='20' x='4' y='2' rx='2' ry='2'/%3E%3Cpath d='M9 22v-4h6v4'/%3E%3Cpath d='M8 6h.01'/%3E%3Cpath d='M16 6h.01'/%3E%3Cpath d='M12 6h.01'/%3E%3Cpath d='M12 10h.01'/%3E%3Cpath d='M12 14h.01'/%3E%3Cpath d='M16 10h.01'/%3E%3Cpath d='M16 14h.01'/%3E%3Cpath d='M8 10h.01'/%3E%3Cpath d='M8 14h.01'/%3E%3C/svg%3E");
}

.icon-map {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpolygon points='3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21'/%3E%3Cline x1='9' x2='9' y1='3' y2='18'/%3E%3Cline x1='15' x2='15' y1='6' y2='21'/%3E%3C/svg%3E");
}

.icon-mine-active {
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='%232563eb' stroke='%232563eb' stroke-width='2'%3E%3Cpath d='M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2'/%3E%3Ccircle cx='12' cy='7' r='4'/%3E%3C/svg%3E");
}

.tabbar-text {
	font-size: 22rpx;
	color: #9ca3af;
}

.tabbar-text.active {
	color: #2563eb;
}
</style>
