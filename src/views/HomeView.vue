<template>
  <div class="flowing-bg">
    <div class="card">
      <div class="avatar-box">
        <img src="/avatar.png" alt="avatar" class="avatar">
        <div class="name">name</div>
        <div class="mail">mail</div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 无需额外逻辑
</script>

<style scoped>

.avatar-box {
  padding: 20px;
}
.card {
  width: 90%;
  height: 80vh;
  padding: 20px;
  background: white;
  border-radius: 16px;  /* 圆角 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  /* 阴影 */
  transition: all 0.3s ease;  /* 过渡动画 */

}
.avatar{
  grid-column: span 1;
  grid-row: span1;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.30);
  transition: all 0.3s ease;
  cursor: pointer;
}
.name {
  grid-column: span 2;
}
.avatar:hover{
  transform: translateY(-8px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.card:hover {
  transform: translateY(-8px);  /* 向上移动8px */
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);  /* 阴影加深 */
}


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
</style>