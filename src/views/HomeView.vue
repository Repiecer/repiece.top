<template>
  <div class="home">
    <!-- 流动背景 -->
    <div class="animated-bg"></div>
    
    <!-- 主要内容 -->
    <div class="content">
      <div class="profile-card">
        <!-- 头像区域 -->
        <div class="avatar-wrapper">
          <div class="avatar-glow"></div>
          <img 
            src="/avatar.png" 
            alt="头像" 
            class="avatar"
            @error="handleImageError"
          />
        </div>
        
        <!-- 姓名 -->
        <h1 class="name">Repiece</h1>
        <p class="title">全栈开发者 | 创作者</p>
        <router-link to="/shop">Shopping</router-link>
        <!-- 分割线 -->
        <div class="divider"></div>
        
        <!-- 联系方式 -->
        <div class="contact-info">
          <div class="contact-item">
            <div class="contact-icon">📧</div>
            <div class="contact-details">
              <div class="contact-label">邮箱</div>
              <a href="mailto:your@email.com" class="contact-value">340508578@qq.com</a>
            </div>
          </div>
          
          <div class="contact-item">
            <div class="contact-icon">📱</div>
            <div class="contact-details">
              <div class="contact-label">电话</div>
              <a href="tel:+86 123 4567 8901" class="contact-value">+86 18270798574</a>
            </div>
          </div>
          
          <div class="contact-item">
            <div class="contact-icon">💬</div>
            <div class="contact-details">
              <div class="contact-label">微信</div>
              <span class="contact-value">340508578</span>
            </div>
          </div>
          
          <div class="contact-item">
            <div class="contact-icon">🐙</div>
            <div class="contact-details">
              <div class="contact-label">GitHub</div>
              <a href="https://github.com/Repiecer" target="_blank" class="contact-value">github.com/Repiecer</a>
            </div>
          </div>
        </div>
        
        <!-- 社交链接 -->
        <div class="social-links">
          <a href="#" class="social-link" title="微博">
            <span>📱</span>
          </a>
          <a href="#" class="social-link" title="公众号">
            <span>📝</span>
          </a>
          <a href="#" class="social-link" title="知乎">
            <span>💡</span>
          </a>
          <a href="#" class="social-link" title="B站">
            <span>🎬</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const handleImageError = (e) => {
  // 如果图片加载失败，显示默认头像
  e.target.src = 'https://via.placeholder.com/200x200/FF6B6B/FFFFFF?text=Avatar'
}
</script>

<style scoped>
.home {
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI', 'PingFang SC', Roboto, 'Helvetica Neue', sans-serif;
}

/* 流动彩色背景 */
.animated-bg {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(125deg, 
    #FF6B6B 0%, 
    #FF8E53 15%, 
    #FFB347 30%, 
    #F4A261 45%, 
    #E9C46A 60%, 
    #95CDB9 75%, 
    #FFA5AB 90%,
    #FF6B6B 100%
  );
  background-size: 400% 400%;
  animation: flowGradient 12s ease infinite;
  z-index: 0;
}

/* 添加叠加层增强可读性 */
.animated-bg::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(255,255,255,0.2) 0%, rgba(0,0,0,0.1) 100%);
  backdrop-filter: blur(2px);
}

@keyframes flowGradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* 内容容器 */
.content {
  position: relative;
  z-index: 1;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

/* 个人卡片 */
.profile-card {
  max-width: 600px;
  width: 100%;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(20px);
  border-radius: 48px;
  padding: 48px 40px;
  text-align: center;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  animation: fadeInUp 0.6s ease;
}

.profile-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 35px 60px -15px rgba(0, 0, 0, 0.3);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 头像区域 */
.avatar-wrapper {
  position: relative;
  display: inline-block;
  margin-bottom: 24px;
}

.avatar {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid white;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
  position: relative;
  z-index: 2;
  transition: transform 0.3s ease;
}

.avatar:hover {
  transform: scale(1.05);
}

.avatar-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background: linear-gradient(135deg, #FF6B6B, #FFB347, #95CDB9);
  opacity: 0.6;
  filter: blur(20px);
  z-index: 1;
  animation: pulse 2s ease infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.4;
    transform: translate(-50%, -50%) scale(1);
  }
  50% {
    opacity: 0.8;
    transform: translate(-50%, -50%) scale(1.1);
  }
}

/* 姓名和标题 */
.name {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 16px 0 8px;
  background: linear-gradient(135deg, #FF6B6B, #FF8E53, #FFB347);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  letter-spacing: 2px;
}

.title {
  font-size: 1rem;
  color: #666;
  margin-bottom: 32px;
  font-weight: 400;
  letter-spacing: 1px;
}

/* 分割线 */
.divider {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #FF6B6B, #FFB347, #95CDB9);
  margin: 24px auto;
  border-radius: 3px;
}

/* 联系方式 */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 32px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 20px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 20px;
  transition: all 0.3s ease;
  text-align: left;
}

.contact-item:hover {
  background: rgba(255, 255, 255, 0.9);
  transform: translateX(8px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.contact-icon {
  font-size: 2rem;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #FF6B6B, #FFB347);
  border-radius: 16px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.contact-details {
  flex: 1;
}

.contact-label {
  font-size: 0.75rem;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 4px;
}

.contact-value {
  font-size: 1rem;
  font-weight: 500;
  color: #333;
  text-decoration: none;
  transition: color 0.2s ease;
}

.contact-value:hover {
  color: #FF6B6B;
}

/* 社交链接 */
.social-links {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.social-link {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #FF6B6B, #FFB347);
  border-radius: 50%;
  text-decoration: none;
  font-size: 1.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.social-link:hover {
  transform: translateY(-4px) scale(1.1);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .profile-card {
    padding: 32px 24px;
  }
  
  .avatar {
    width: 120px;
    height: 120px;
  }
  
  .avatar-glow {
    width: 140px;
    height: 140px;
  }
  
  .name {
    font-size: 2rem;
  }
  
  .contact-item {
    padding: 10px 16px;
  }
  
  .contact-icon {
    font-size: 1.5rem;
    width: 40px;
    height: 40px;
  }
  
  .contact-value {
    font-size: 0.9rem;
  }
}
</style>