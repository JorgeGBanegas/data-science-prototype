<template>
  <div class="home-page">
    <header class="bg-primary text-light py-5">
      <div class="container text-center">
        <h1 class="display-4">Plataforma de Valuación Inmobiliaria</h1>
        <p class="lead">Valora propiedades de manera rápida y precisa.</p>
        <router-link to="/valoraciones" class="btn btn-light btn-lg">Comenzar</router-link>
      </div>
    </header>

    <section class="py-5">
      <div class="container text-center">
        <h2 class="mb-4">¿Cómo funciona?</h2>
        <div class="row">
          <div class="col-md-4">
            <div class="card mb-4">
              <div class="card-body">
                <h4 class="card-title">Paso 1</h4>
                <p class="card-text">Ingresa los detalles de la propiedad.</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card mb-4">
              <div class="card-body">
                <h4 class="card-title">Paso 2</h4>
                <p class="card-text">Analiza la información y calcula la valuación.</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card mb-4">
              <div class="card-body">
                <h4 class="card-title">Paso 3</h4>
                <p class="card-text">Obtén el valor estimado de la propiedad.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "HomePage"
};
</script>

<style>
.home-page {
  text-align: center;
}

.header-bg {
  background-color: #343a40;
}
</style>
