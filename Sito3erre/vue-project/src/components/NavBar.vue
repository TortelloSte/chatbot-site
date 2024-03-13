<template>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    <header>
    
      <div class="logo">Logo</div>
      <nav :class="{ 'hidden': isMenuHidden }">
        <ul>
          <li><a href="#sicurezza">Sicurezza</a></li>
          <li><a href="#cancelli">Cancelli/Recensioni</a></li>
          <li><a href="#carpenteria">Carpenteria</a></li>
          <li><a href="#lavori">I nostri lavori</a></li>
        </ul>
      </nav>
      <button class="hamburger" @click="toggleMenu">&#9776;</button>
    </header>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  
  const isMenuHidden = ref(false);
  
  function toggleMenu() {
    isMenuHidden.value = !isMenuHidden.value;
  }
  </script>
  
  <style scoped>
  
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    color: #000000;
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    font-style: normal;
  }
  
  .logo {
    font-size: 24px;
  }
  
  nav ul {
    list-style-type: none;
    display: flex;
  }
  
  nav ul li {
    margin-right: 20px;
  }
  
  nav ul li a {
    text-decoration: none;
    color: #000000;
  }
  
  nav ul li a:hover {
    color: #db8f2a;
  }
  
  .hamburger {
    display: none;
    background: none;
    border: none;
    font-size: 24px;
    color: #000000;
  }
  
  @media (max-width: 582px) {
    nav ul {
      display: none;
    }
  
    .hamburger {
      display: block;
    }
  }
  </style>
  
  