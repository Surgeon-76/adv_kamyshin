<template>
  <nav class="navbar fixed-top  navbar-dark bg-primary navbar-expand-lg ">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">LOGO</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarScroll">
      <ul class="navbar-nav me-auto my-2 my-lg-0 " >
        <li class="nav-item">

          <nuxt-link :class="{active:$route.path == '/'}" class="nav-link " aria-current="page"  to="/">Главная</nuxt-link>
        </li>
        <li class="nav-item">
          <nuxt-link class="nav-link " :class="{active:$route.path == '/estate'}" aria-current="page"  to="/estate">Недвижимость</nuxt-link>

        </li>
        <li class="nav-item">
          <nuxt-link class="nav-link " :class="{active:$route.path == '/services'}"  aria-current="page"  to="/services">Услуги</nuxt-link>

        </li>

        <li class="nav-item soon">
          <div class="soon-card"><span>Скоро</span></div>
          <span class="nav-link "  aria-current="page" >Работа</span>

        </li>
        <li class="nav-item soon">
          <div class="soon-card"><span>Скоро</span></div>
          <span class="nav-link "  aria-current="page" >Авто</span>

        </li>
        <li class="nav-item soon">
          <div class="soon-card"><span>Скоро</span></div>
          <span class="nav-link "  aria-current="page" >Новости</span>

        </li>
        <li class="nav-item soon">
          <div class="soon-card"><span>Скоро</span></div>
          <span class="nav-link "  aria-current="page" >Отзовик</span>

        </li>
        <li class="nav-item soon">
          <div class="soon-card"><span>Скоро</span></div>
          <span class="nav-link "  aria-current="page" >Обсуждения</span>

        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarScrollingDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Войти
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarScrollingDropdown">
            <li>
            <nuxt-link class="dropdown-item"  to="/profile">Личный кабинет</nuxt-link>
            </li>
            <li><a class="dropdown-item" href="#">Выйти</a></li>
          </ul>
        </li>
      </ul>
             <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Поиск" aria-label="Search">

      </form>
    </div>
  </div>
</nav>
</template>


<style lang="scss" scoped>
  .soon{
    position: relative;
  }
  .soon-card{
    position: absolute;
    right: -1em;
    top: -.5em;
    font-size: .6em;
    background: white;
    padding: .2em;
    border-radius: 12px;
  }
</style>
