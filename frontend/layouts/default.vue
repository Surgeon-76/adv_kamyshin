<template>
  <div id="app">
    <header>
      <Navbar />
    </header>
    <main>
      <div style="margin-top:4em" class="container"><Nuxt/></div>

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
