<template>
    <div class="services-container">
      <h2 class="title">I nostri <span class="orange-text">servizi</span></h2>
      <div class="images-container">
        <div class="service">
          <h3 class="service-title">INFERIATE SU MISURA</h3>
          <img :src="Rectangle1" alt="Servizio 1">
        </div>
        <div class="service">
          <h3 class="service-title">ARREDI IN FERRO</h3>
          <img :src="Rectangle2" alt="Servizio 2">
        </div>
        <div class="service">
          <h3 class="service-title">CANCELLI E RECIZIONI</h3>
          <img :src="Rectangle3" alt="Servizio 3">
        </div>
      </div>
    </div>
  </template>

  <script setup>
  import Rectangle1 from '../assets/Rectangle (1).png'
  import Rectangle2 from '../assets/Rectangle (2).png'
  import Rectangle3 from '../assets/Rectangle (3).png'


  </script>
  
  <style scoped>
    .services-container {
        text-align: left;
        background-color: black;
    }
  
    .title {
        font-size: 45px;
        margin-bottom: 20px;
        color: white;
        margin-left: 50px;
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        margin-top: 40px;
    }
  
    .images-container {
        display: flex;
        justify-content: center; /* Centra le immagini */
        flex-wrap: wrap;
    }
  
    .service {
        margin-left: 40px;
        margin-right: 40px;
        margin-bottom: 20px;
        width: calc(33.33% - 80px);
    }
  
    .service-title {
        font-size: 29px;
        margin-bottom: 10px;
        color: white;
        font-family: "Poppins", sans-serif;
        font-weight: 250;
    }

    .orange-text {
        color: orange;
    }

    @media (max-width: 768px) {
        .service {
            width: 100%;
           
        }
    }
</style>