<template>
    <header>
      
    </header>
  
    <main>
      <div class="container">
        <div class="title-section">
          <h2>Chi siamo?</h2>
          <p>3Erre Saldature Srl è un'azienda nata nel 1995, e attiva in tutta la Monza Brianza e nelle zone vicine, come Saronno, specializzata in opere da fabbro e di carpenteria metallica, quali inferriate e grate di sicurezza fisse, scorrevoli e con snodo, recinzioni, cancelli scorrevoli, a battente e pedonali, ringhiere, parapetti, serramenti in PVC e legno/alluminio, tapparelle, persiane, zanzariere, copricontatori e molto altro ancora.</p>
        </div>
        <div class="image-section">
          <img :src="Foto" alt="Immagine Chi Siamo">
        </div>
      </div>
    </main>
</template>

<script setup>
import Foto from '../assets/Foto 3.png';
</script>


<style scoped>
.container {
  margin-top: 110px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  justify-content: flex-end;
}

.title-section {
  flex: 1;
  padding-right: 20px;
  margin-left: 50px;
}

.title-section h2 {
  font-size: 35px;
  margin-bottom: 10px;
  font-family: "Poppins", sans-serif;
  font-weight: 400;
}

.title-section p {
  font-size: 23px;
  line-height: 1.5;
  font-family: "Poppins", sans-serif;
}

.image-section {
  flex: 1;
  display: flex;
  justify-content: flex-end;
  
}

.image-section img {
  max-width: 100%;
  height: auto;
  border-radius: 50px;
}

@media (max-width: 768px) {
  .image-section {
    display: none;
  }
}

</style>
