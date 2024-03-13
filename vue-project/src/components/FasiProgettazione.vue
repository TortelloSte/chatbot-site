<template>
    <header>
        <h1>Fasi della <span class="orange"> progettazione</span></h1>
    </header>
  
    <main>
        <div class="content">
            <div class="left">
                <p>In questa fase, insieme al cliente, capiamo la soluzione migliore da adottare</p>
            </div>
            <div class="right">
                <div class="circle">Misure</div>
            </div>
        </div>

       <div class="content">
            <div class="right">
                <div class="circle">Fase di sviluppo</div>
            </div>
            <div class="left">
                <p>Dopo aver deciso la migliore soluzione inziamo lo sviluppo del prodotto</p>
            </div>
        </div>

        <div class="content">
            <div class="left">
                <p>Ci teniamo a seguire dall’inizio alla fine tutte le nostre creazioni, al montaggio ci pensiamo noi di 3Erre</p>
            </div>
            <div class="right">
                <div class="circle">Montaggio</div>
            </div>
        </div>
        
        
    </main>
</template>


<style scoped>
  .content {
    display: flex;
    justify-content: center; 
    align-items: center; 
    margin-top: 100px; 
  }

  .left, .right {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .left {
    margin-right: 20px;
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 25px;
    width: 500px;
  }

  .right {
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 25px; 
  }

  .right .circle {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 292px; 
    height: 281px; 
    border: 2px solid #FFA500; 
    border-radius: 50%; 
    font-size: 20px; 
    color: #000000; 
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 25px;
    
  }

  h1 {
    margin-left: 87px;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
    font-style: normal;
    font-size: 45px;
  }

  .orange {
    color: orange;
  }

  @media only screen and (max-width: 600px) {
    .content {
      flex-direction: column;
      text-align: center;
    }
    h1 {
    margin-left: 50px;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
    font-style: normal;
    font-size: 30px;
  }

    .left, .right {
      margin: 0;
    }

    .left {
      width: auto;
    }

    .right {
      display: none;
    }

    .right .circle {
      display: flex;
    }
  }
</style>

<script setup>
   
</script>







