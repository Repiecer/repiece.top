<template>
  <div class="shipping-app">
    <!-- 头部导航 -->
    <div class="nav-bar">
      <h2>nb📦 AI拼单互助平台</h2>
      <div class="nav-tabs">
        <button 
          :class="['tab-btn', { active: activeTab === 'browse' }]"
          @click="activeTab = 'browse'"
        >
          浏览请求
        </button>
        <button 
          :class="['tab-btn', { active: activeTab === 'my-pickups' }]"
          @click="activeTab = 'my-pickups'"
        >
          我的接取
        </button>
      </div>
    </div>

    <!-- 浏览请求页面 -->
    <div v-if="activeTab === 'browse'" class="browse-section">
      <!-- 搜索栏 -->
      <div class="search-bar">
        <input 
          v-model="searchKeyword" 
          type="text" 
          placeholder="搜索商品名称..."
          @keyup.enter="handleSearch"
        />
        <button @click="handleSearch">🔍 搜索</button>
        <button class="publish-btn" @click="showPublishForm = true">➕ 发布请求</button>
      </div>

      <!-- 卡片列表 -->
      <div class="cards-grid">
        <div 
          v-for="request in requests" 
          :key="request.id" 
          class="request-card"
          :style="{ animationDelay: `${index * 0.05}s` }"
        >
          <div class="card-header">
            <h3>{{ request.product_name }}</h3>
            <span class="priority-badge" :class="'priority-' + request.priority">
              {{ getPriorityText(request.priority) }}
            </span>
          </div>
          
          <div class="card-body">
            <p class="product-link">
              🔗 <a :href="request.product_url" target="_blank">查看商品</a>
            </p>
            <p class="people-count">
              👥 已接取: {{ request.current_people }} / {{ request.max_people }}
            </p>
            <p class="description">{{ request.description }}</p>
          </div>
          
          <div class="card-footer">
            <button 
              class="detail-btn" 
              @click="showDetail(request)"
            >
              查看详情
            </button>
            <button 
              class="pickup-btn"
              :disabled="request.current_people >= request.max_people"
              @click="handlePickup(request)"
            >
              {{ request.current_people >= request.max_people ? '已满员' : '📌 接取' }}
            </button>
          </div>
        </div>
        
        <div v-if="requests.length === 0 && !loading" class="empty-state">
          <p>暂无拼单请求，发布第一个吧！</p>
        </div>
      </div>
    </div>

    <!-- 我的接取页面 -->
    <div v-if="activeTab === 'my-pickups'" class="pickups-section">
      <div class="cards-grid">
        <div 
          v-for="pickup in myPickups" 
          :key="pickup.id" 
          class="request-card"
        >
          <div class="card-header">
            <h3>{{ pickup.product_name }}</h3>
          </div>
          <div class="card-body">
            <p class="product-link">
              🔗 <a :href="pickup.product_url" target="_blank">查看商品</a>
            </p>
            <p class="publisher-info">
              发布者: {{ pickup.publisher_name || '匿名' }}
            </p>
            <button class="contact-btn" @click="showContact(pickup)">
              📞 联系方式
            </button>
          </div>
        </div>
        
        <div v-if="myPickups.length === 0" class="empty-state">
          <p>暂无接取的请求</p>
        </div>
      </div>
    </div>

    <!-- 发布表单弹窗 -->
    <div v-if="showPublishForm" class="modal" @click.self="showPublishForm = false">
      <div class="modal-content">
        <h3>发布拼单请求</h3>
        <form @submit.prevent="submitRequest">
          <div class="form-group">
            <label>商品名称 *</label>
            <input v-model="newRequest.product_name" type="text" required />
          </div>
          
          <div class="form-group">
            <label>商品链接 *</label>
            <input v-model="newRequest.product_url" type="url" required />
          </div>
          
          <div class="form-group">
            <label>接取上限人数 *</label>
            <input v-model.number="newRequest.max_people" type="number" min="1" required />
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>手机号 *</label>
              <input v-model="newRequest.phone" type="tel" required />
            </div>
            <div class="form-group">
              <label>QQ *</label>
              <input v-model="newRequest.qq" type="text" required />
            </div>
          </div>
          
          <div class="form-group">
            <label>优先级</label>
            <select v-model="newRequest.priority">
              <option :value="0">普通</option>
              <option :value="1">紧急</option>
              <option :value="2">特急</option>
            </select>
          </div>
          
          <div class="form-group">
            <label>详细说明</label>
            <textarea v-model="newRequest.description" rows="3"></textarea>
          </div>
          
          <div class="form-group">
            <label>您的称呼</label>
            <input v-model="newRequest.publisher_name" type="text" placeholder="选填" />
          </div>
          
          <div class="form-buttons">
            <button type="button" @click="showPublishForm = false">取消</button>
            <button type="submit" :disabled="submitting">发布</button>
          </div>
        </form>
      </div>
    </div>

    <!-- 详情弹窗 -->
    <div v-if="showDetailModal" class="modal" @click.self="showDetailModal = false">
      <div class="modal-content detail-modal">
        <h3>📋 请求详情</h3>
        <div class="detail-info">
          <p><strong>商品名称：</strong>{{ currentRequest.product_name }}</p>
          <p><strong>商品链接：</strong><a :href="currentRequest.product_url" target="_blank">{{ currentRequest.product_url }}</a></p>
          <p><strong>接取人数：</strong>{{ currentRequest.current_people }} / {{ currentRequest.max_people }}</p>
          <p><strong>优先级：</strong>{{ getPriorityText(currentRequest.priority) }}</p>
          <p><strong>详细说明：</strong>{{ currentRequest.description || '无' }}</p>
          
          <div class="contact-info-detail">
            <p><strong>联系方式：</strong></p>
            <div class="contact-row">
              📱 手机号: {{ currentRequest.phone }}
              <button class="copy-btn" @click="copyToClipboard(currentRequest.phone)">复制</button>
            </div>
            <div class="contact-row">
              💬 QQ: {{ currentRequest.qq }}
              <button class="copy-btn" @click="copyToClipboard(currentRequest.qq)">复制</button>
            </div>
          </div>
        </div>
        <div class="modal-buttons">
          <button @click="showDetailModal = false">关闭</button>
        </div>
      </div>
    </div>

    <!-- 联系方式弹窗（我的接取） -->
    <div v-if="showContactModal" class="modal" @click.self="showContactModal = false">
      <div class="modal-content contact-modal">
        <h3>📞 发布者联系方式</h3>
        <div class="contact-row">
          📱 手机号: {{ contactInfo.phone }}
          <button class="copy-btn" @click="copyToClipboard(contactInfo.phone)">复制</button>
        </div>
        <div class="contact-row">
          💬 QQ: {{ contactInfo.qq }}
          <button class="copy-btn" @click="copyToClipboard(contactInfo.qq)">复制</button>
        </div>
        <div class="modal-buttons">
          <button @click="showContactModal = false">关闭</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// API 配置 - 修改为你的后端地址
const API_BASE = 'https://repiece.top/api'

// 状态
const activeTab = ref('browse')
const searchKeyword = ref('')
const requests = ref([])
const myPickups = ref([])
const loading = ref(false)
const submitting = ref(false)
const showPublishForm = ref(false)
const showDetailModal = ref(false)
const showContactModal = ref(false)
const currentRequest = ref({})
const contactInfo = ref({})

// 新请求表单
const newRequest = ref({
  product_name: '',
  product_url: '',
  max_people: 1,
  phone: '',
  qq: '',
  priority: 0,
  description: '',
  publisher_name: ''
})

// 获取当前用户标识（使用 localStorage）
const getUserId = () => {
  let userId = localStorage.getItem('shipping_user_id')
  if (!userId) {
    userId = 'user_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9)
    localStorage.setItem('shipping_user_id', userId)
  }
  return userId
}

// 获取所有请求
const fetchRequests = async () => {
  loading.value = true
  try {
    const params = searchKeyword.value ? { search: searchKeyword.value } : {}
    const res = await axios.get(`${API_BASE}/requests`, { params })
    requests.value = res.data
  } catch (error) {
    console.error('获取请求失败:', error)
  } finally {
    loading.value = false
  }
}

// 获取我的接取
const fetchMyPickups = async () => {
  try {
    const userId = getUserId()
    const res = await axios.get(`${API_BASE}/pickups/${userId}`)
    myPickups.value = res.data
  } catch (error) {
    console.error('获取接取列表失败:', error)
  }
}

// 发布请求
const submitRequest = async () => {
  if (!newRequest.value.product_name || !newRequest.value.product_url || 
      !newRequest.value.phone || !newRequest.value.qq) {
    alert('请填写必填项')
    return
  }
  
  submitting.value = true
  try {
    const userId = getUserId()
    await axios.post(`${API_BASE}/requests`, {
      ...newRequest.value,
      publisher_id: userId
    })
    alert('发布成功！')
    showPublishForm.value = false
    newRequest.value = {
      product_name: '',
      product_url: '',
      max_people: 1,
      phone: '',
      qq: '',
      priority: 0,
      description: '',
      publisher_name: ''
    }
    fetchRequests()
  } catch (error) {
    console.error('发布失败:', error)
    alert('发布失败，请重试')
  } finally {
    submitting.value = false
  }
}

// 接取请求
const handlePickup = async (request) => {
  if (request.current_people >= request.max_people) {
    alert('该请求已满员')
    return
  }
  
  try {
    const userId = getUserId()
    await axios.post(`${API_BASE}/pickups`, {
      request_id: request.id,
      user_id: userId
    })
    alert('接取成功！')
    fetchRequests()
  } catch (error) {
    console.error('接取失败:', error)
    alert(error.response?.data?.detail || '接取失败，请重试')
  }
}

// 显示详情
const showDetail = (request) => {
  currentRequest.value = request
  showDetailModal.value = true
}

// 显示联系方式（我的接取）
const showContact = (pickup) => {
  contactInfo.value = {
    phone: pickup.publisher_phone,
    qq: pickup.publisher_qq
  }
  showContactModal.value = true
}

// 搜索
const handleSearch = () => {
  fetchRequests()
}

// 复制到剪贴板
const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text)
    alert('已复制到剪贴板')
  } catch (err) {
    console.error('复制失败:', err)
    alert('复制失败，请手动复制')
  }
}

// 优先级文本
const getPriorityText = (priority) => {
  const map = { 0: '普通', 1: '紧急', 2: '特急' }
  return map[priority] || '普通'
}

onMounted(() => {
  fetchRequests()
})
</script>

<style scoped>
.shipping-app {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* 导航栏 */
.nav-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 2px solid #f0f0f0;
  flex-wrap: wrap;
  gap: 15px;
}

.nav-bar h2 {
  margin: 0;
  background: linear-gradient(135deg, #FF6B6B, #FF8E53);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.nav-tabs {
  display: flex;
  gap: 10px;
}

.tab-btn {
  padding: 10px 24px;
  border: none;
  background: #f5f5f5;
  border-radius: 30px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.tab-btn.active {
  background: linear-gradient(135deg, #FF6B6B, #FF8E53);
  color: white;
}

/* 搜索栏 */
.search-bar {
  display: flex;
  gap: 12px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.search-bar input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid #ddd;
  border-radius: 30px;
  font-size: 14px;
}

.search-bar button {
  padding: 12px 24px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.search-bar button:first-of-type {
  background: #f0f0f0;
}

.publish-btn {
  background: linear-gradient(135deg, #FF6B6B, #FF8E53);
  color: white;
}

/* 卡片网格 */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 24px;
}

.request-card {
  background: white;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
  animation: fadeInUp 0.4s ease forwards;
  opacity: 0;
}

.request-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.card-header h3 {
  margin: 0;
  font-size: 18px;
  color: #333;
}

.priority-badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
}

.priority-0 { background: #e0e0e0; color: #666; }
.priority-1 { background: #FFE5B4; color: #E67E22; }
.priority-2 { background: #FFCDD2; color: #E74C3C; }

.card-body {
  margin-bottom: 16px;
}

.product-link a {
  color: #FF6B6B;
  text-decoration: none;
}

.people-count {
  color: #666;
  font-size: 14px;
  margin: 8px 0;
}

.description {
  color: #777;
  font-size: 14px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-footer {
  display: flex;
  gap: 12px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.detail-btn, .pickup-btn, .contact-btn {
  flex: 1;
  padding: 8px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.detail-btn {
  background: #f5f5f5;
}

.pickup-btn, .contact-btn {
  background: linear-gradient(135deg, #FF6B6B, #FF8E53);
  color: white;
}

.pickup-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

/* 模态框 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.2s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-content {
  background: white;
  border-radius: 24px;
  padding: 32px;
  max-width: 500px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-content h3 {
  margin-top: 0;
  margin-bottom: 20px;
}

/* 表单 */
.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 6px;
  font-size: 14px;
  font-weight: 500;
}

.form-group input, .form-group select, .form-group textarea {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 12px;
  font-size: 14px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.form-buttons, .modal-buttons {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 20px;
}

.form-buttons button, .modal-buttons button {
  padding: 10px 24px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}

.form-buttons button:first-child, .modal-buttons button {
  background: #f0f0f0;
}

.form-buttons button:last-child {
  background: linear-gradient(135deg, #FF6B6B, #FF8E53);
  color: white;
}

/* 详情弹窗 */
.contact-info-detail {
  background: #f9f9f9;
  padding: 16px;
  border-radius: 16px;
  margin-top: 16px;
}

.contact-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
}

.copy-btn {
  background: #f0f0f0;
  border: none;
  padding: 4px 12px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 12px;
}

.empty-state {
  text-align: center;
  padding: 60px;
  color: #999;
}

/* 响应式 */
@media (max-width: 768px) {
  .cards-grid {
    grid-template-columns: 1fr;
  }
  
  .nav-bar {
    flex-direction: column;
    text-align: center;
  }
  
  .search-bar {
    flex-direction: column;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>