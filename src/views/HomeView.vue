<template>
  <div class="flowing-bg">
    <div class="card">
      <div class="avatar-box">
        <!-- 左侧头像区域 -->
        <div class="avatar-wrapper">
          <img src="/avatar.png" alt="avatar" class="avatar">
          <div class="avatar-decoration"></div>
        </div>
        
        <!-- 右侧内容区域 -->
        <div class="info-section">
          <!-- 姓名与称号 -->
          <div class="header-section">
            <h1 class="name">Repiece</h1>
            <p class="title">全栈开发者 / 开源爱好者</p>
            <div class="divider"></div>
          </div>

          <!-- 联系方式卡片 -->
          <div class="contact-card">
            <div class="contact-item email-item" @click="copyEmail">
              <div class="contact-icon">📧</div>
              <div class="contact-content">
                <span class="contact-label">电子邮箱</span>
                <span class="contact-value">340508578@qq.com</span>
              </div>
              <div class="copy-badge" v-if="showCopyTip">已复制</div>
            </div>
            <div class="contact-item">
              <div class="contact-icon">📍</div>
              <div class="contact-content">
                <span class="contact-label">所在城市</span>
                <span class="contact-value">中国 · 南京</span>
              </div>
            </div>
            <div class="contact-item">
              <div class="contact-icon">💼</div>
              <div class="contact-content">
                <span class="contact-label">工作经验</span>
                <span class="contact-value">0年全栈开发经验</span>
              </div>
            </div>
          </div>

          <!-- 关于我 -->
          <div class="bio-section">
            <h3 class="section-title">
              <span class="title-icon">✨</span>
              关于我
            </h3>
            <p class="bio-text">
              热爱编程与设计，追求优雅的代码和出色的用户体验。我相信技术的力量可以改变世界，
              也相信每一个细节都值得被认真对待。除了编码，我还喜欢分享知识、参与开源社区，
              持续学习新技术，保持对创造的热情。
            </p>
          </div>

          <!-- 技术栈 -->
          <div class="skills-section">
            <h3 class="section-title">
              <span class="title-icon">⚡</span>
              技术栈
            </h3>
            <div class="skills-grid">
              <div class="skill-category">
                <p class="category-title">前端</p>
                <div class="skill-tags">
                  <span class="tag">Vue.js</span>
                  <span class="tag">React</span>
                  <span class="tag">TypeScript</span>
                  <span class="tag">Tailwind CSS</span>
                  <span class="tag">Nuxt.js</span>
                </div>
              </div>
              <div class="skill-category">
                <p class="category-title">后端</p>
                <div class="skill-tags">
                  <span class="tag">Node.js</span>
                  <span class="tag">Python</span>
                  <span class="tag">Express</span>
                  <span class="tag">MongoDB</span>
                  <span class="tag">PostgreSQL</span>
                </div>
              </div>
              <div class="skill-category">
                <p class="category-title">工具</p>
                <div class="skill-tags">
                  <span class="tag">Git</span>
                  <span class="tag">Docker</span>
                  <span class="tag">VS Code</span>
                </div>
              </div>
              <div class="skill-category">
                <p class="category-title">项目</p>
                <div class="skill-tags">
                  <router-link to="shop" class="tag">Shop</router-link>
                </div>
              </div>
            </div>
          </div>

          <!-- 社交链接 -->
          <div class="social-section">
            <a href="#" class="social-link">GitHub</a>
            <a href="#" class="social-link">掘金</a>
            <a href="#" class="social-link">Twitter</a>
            <a href="#" class="social-link">博客</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const showCopyTip = ref(false)

const copyEmail = () => {
  const email = '340508578@qq.com'
  navigator.clipboard.writeText(email).then(() => {
    showCopyTip.value = true
    setTimeout(() => {
      showCopyTip.value = false
    }, 2000)
  }).catch(() => {
    const textarea = document.createElement('textarea')
    textarea.value = email
    document.body.appendChild(textarea)
    textarea.select()
    document.execCommand('copy')
    document.body.removeChild(textarea)
    showCopyTip.value = true
    setTimeout(() => {
      showCopyTip.value = false
    }, 2000)
  })
}
</script>

<style scoped>
/* ========== 字体系统 ========== */
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700&family=Space+Grotesk:wght@400;500;600&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* 保持原有卡片大小和背景 */
.avatar-box {
  padding: 80px;
}

.card {
  width: 90%;
  height: 80vh;
  padding: 20px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  overflow-y: auto;
  font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* 自定义滚动条 */
.card::-webkit-scrollbar {
  width: 8px;
}

.card::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}

.card::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
  border-radius: 10px;
}

.card::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #ff5252, #3eb9b0);
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

/* 头像样式 */
.avatar-wrapper {
  position: relative;
}

.avatar {
  width: 400px;
  height: 400px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
  transition: all 0.4s cubic-bezier(0.2, 0.9, 0.4, 1.1);
  cursor: pointer;
  position: relative;
  z-index: 2;
}

.avatar-decoration {
  position: absolute;
  top: -10px;
  left: -10px;
  right: -10px;
  bottom: -10px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ff6b6b, #4ecdc4, #45b7d1);
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: 1;
}

.avatar-wrapper:hover .avatar {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 30px 50px rgba(0, 0, 0, 0.3);
}

.avatar-wrapper:hover .avatar-decoration {
  opacity: 0.3;
}

/* 布局：头像和内容并排 */
.avatar-box {
  display: flex;
  gap: 60px;
  align-items: flex-start;
  flex-wrap: wrap;
  justify-content: center;
}

/* 右侧信息区域 */
.info-section {
  flex: 1;
  min-width: 320px;
  display: flex;
  flex-direction: column;
  gap: 32px;
  padding-top: 20px;
}

/* 头部区域 */
.header-section {
  margin-bottom: 8px;
}

.name {
  font-family: 'Space Grotesk', 'Inter', monospace;
  font-size: 48px;
  font-weight: 700;
  background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  margin-bottom: 12px;
  letter-spacing: -0.02em;
}

.title {
  font-size: 18px;
  color: #6c757d;
  font-weight: 500;
  margin-bottom: 16px;
}

.divider {
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
  border-radius: 2px;
}

/* 联系方式卡片 */
.contact-card {
  background: #f8f9fa;
  border-radius: 20px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  transition: all 0.3s ease;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 8px 12px;
  border-radius: 12px;
  transition: all 0.2s ease;
  position: relative;
}

.email-item {
  cursor: pointer;
}

.email-item:hover {
  background: rgba(78, 205, 196, 0.1);
  transform: translateX(4px);
}

.contact-icon {
  font-size: 24px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.contact-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.contact-label {
  font-size: 12px;
  font-weight: 500;
  color: #868e96;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.contact-value {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
}

.copy-badge {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: #4ecdc4;
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-50%) translateX(10px);
  }
  to {
    opacity: 1;
    transform: translateY(-50%) translateX(0);
  }
}

/* 章节标题 */
.section-title {
  font-family: 'Space Grotesk', monospace;
  font-size: 24px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.title-icon {
  font-size: 26px;
}

/* 关于我 */
.bio-section {
  margin-top: 8px;
}

.bio-text {
  font-size: 15px;
  line-height: 1.8;
  color: #495057;
  text-align: justify;
}

/* 技术栈区域 */
.skills-section {
  margin-top: 8px;
}

.skills-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.skill-category {
  background: #f8f9fa;
  border-radius: 16px;
  padding: 16px;
  transition: all 0.3s ease;
}

.skill-category:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}

.category-title {
  font-size: 14px;
  font-weight: 600;
  color: #ff6b6b;
  margin-bottom: 12px;
  letter-spacing: 0.5px;
}

.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag {
  padding: 6px 16px;
  background: white;
  border-radius: 30px;
  font-size: 13px;
  font-weight: 500;
  color: #2c3e50;
  transition: all 0.2s ease;
  cursor: default;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  border: 1px solid #e9ecef;
}

.tag:hover {
  transform: translateY(-2px);
  border-color: #4ecdc4;
  box-shadow: 0 4px 12px rgba(78, 205, 196, 0.2);
  color: #4ecdc4;
}

/* 社交链接 */
.social-section {
  display: flex;
  gap: 20px;
  padding-top: 8px;
  border-top: 1px solid #e9ecef;
  margin-top: 8px;
}

.social-link {
  color: #6c757d;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.2s ease;
  padding: 8px 0;
  position: relative;
}

.social-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
  transition: width 0.3s ease;
}

.social-link:hover {
  color: #ff6b6b;
}

.social-link:hover::after {
  width: 100%;
}

/* 流动背景保持不变 */
.flowing-bg {
  min-height: 100vh;
  background: linear-gradient(
    270deg,
    #ff6b6b,
    #4ecdc4,
    #45b7d1,
    #96ceb4,
    #ff6b6b
  );
  background-size: 400% 400%;
  animation: flow 15s ease infinite;
  display: flex;
  justify-content: center;
  align-items: center;
}

@keyframes flow {
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

/* 响应式设计 */
@media (max-width: 1100px) {
  .avatar {
    width: 320px;
    height: 320px;
  }
  
  .avatar-box {
    gap: 40px;
  }
  
  .name {
    font-size: 40px;
  }
}

@media (max-width: 900px) {
  .avatar {
    width: 280px;
    height: 280px;
  }
  
  .avatar-box {
    gap: 30px;
  }
  
  .info-section {
    min-width: 280px;
  }
}

@media (max-width: 768px) {
  .avatar-box {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .avatar-box {
    padding: 40px;
  }
  
  .info-section {
    align-items: center;
    text-align: center;
    width: 100%;
  }
  
  .divider {
    margin: 0 auto;
  }
  
  .contact-item {
    justify-content: flex-start;
    text-align: left;
  }
  
  .section-title {
    justify-content: center;
  }
  
  .skills-grid {
    width: 100%;
  }
  
  .skill-category {
    text-align: left;
  }
  
  .skill-tags {
    justify-content: center;
  }
  
  .social-section {
    justify-content: center;
  }
}

@media (max-width: 600px) {
  .avatar {
    width: 200px;
    height: 200px;
  }
  
  .name {
    font-size: 32px;
  }
  
  .title {
    font-size: 16px;
  }
  
  .section-title {
    font-size: 20px;
  }
}
</style>