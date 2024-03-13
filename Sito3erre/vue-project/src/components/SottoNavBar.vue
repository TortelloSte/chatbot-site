
<template>
    <header>
      <div class="title-section">
        <h1>Il nuovo concetto di <span class="orange-text">carpenteria<br> metallica</span></h1>
        <p>L'assistente per la sicurezza e il design della tua casa</p>
        <router-link to="/Contattaci"><button>Contattaci</button></router-link>
       
      </div>
    </header>
  
    <main>
      <div class="image-container">
      <img :src="foto1" alt="">
      <img :src="Ellipse1" class="ellipse" alt="">
      <img :src="Ellipse2" class="ellipse" alt="">
      
      </div>
      
    </main>
</template>
  
<script setup>
  
  import foto1 from '../assets/foto1.png';
  import Ellipse1 from '../assets/Ellipse 1.png'
  import Ellipse2 from '../assets/Ellipse 2.png'
  
</script>

<style scoped>
.image-container {
  position: relative;
  width: 100%; 
}
button{ border-radius: 21px;}

.image-container img {
  width: 100%;
  display: block;
  margin-top: 20px;
}

.ellipse {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); 
  height: auto;
  z-index: -1;
}

.title-section {
  text-align: left;
  margin-left: 15px;
  font-family: "Poppins", sans-serif;
}

.title-section h1 {
  font-size: 50px;
  margin-bottom: 10px;
}

.title-section p {
  font-size: 20px;
  margin-bottom: 20px;
}

.title-section button {
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

.title-section button:hover {
  background-color: #555;
}
.orange-text {
  color: orange; 
}
</style>
  