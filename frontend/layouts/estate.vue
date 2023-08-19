<template>
  <div id="app">
    <header>
      <Navbar />
    </header>
    <main>
      <section id="header_index" class="mb-4">
        <div id="header_page">
          <div id="header_page__inner">
            <h1 class="text-center">
              Покупка и продажа недвижимости в Камышине
            </h1>
          </div>
        </div>
      </section>
      <div class="container">
        <h4>Подобрать недвижимость</h4>
        <section id="section-filters">
          <Filters />
        </section>
        <section id="content " class="mt-4">
          <div class="row">
            <div class="col-12 col-lg-8 text-start">
              <Nuxt />
            </div>
            <div class="col-12 col-lg-4 text-end">
        <span style="font-size: 2em">Избранное</span>
        <div class="row justify-content-end">
          <div v-for="i in 4" class="mt-4 col-12 d-flex justify-content-end">
            <Favorites/>
          </div>
        </div>
            </div>
          </div>
        </section>
      </div>
    </main>
    <footer></footer>
  </div>
</template>

<style lang="scss">
#header_index {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: center;
}
#header_page {
  // background-size: auto 40%;
  // background-position: 50% -20%;
  background-image: url("https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80");
  background-position: 50% 0;
  background-repeat: no-repeat;
  background-attachment: fixed;
  box-shadow: 0 1px 5px hsl(0deg 0% 86% / 50%);
  color: white;
  width: 100%;
  height: 100%;
  background-size: 110% !important;
  @media (min-width: 1080.99px) {
    background-size: 100%;
    // background-position: 50% -10%;
  }
  @media (max-width: 1080px) {
    background-size: auto 50%;
    // background-position: 50% 0;
  }
  &__inner {
    background-image: linear-gradient(rgba(0, 0, 0, 0.29), rgba(0, 0, 0, 0.66));
    // padding: 100px 25px;
    height: 25vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
