<template>
  <div class="row box-filter">
    <div class="col-12 col-lg-2">
      <select
        class="form-select form-select-lg mb-3"
        aria-label=".form-select-lg example"
      >
        <option selected>Квартира</option>
        <option value="1">Дом</option>
      </select>
    </div>

    <div class="col-12 col-lg-2">
      <select
        class="form-select form-select-lg mb-3"
        aria-label=".form-select-lg example"
      >
        <option selected>Купить</option>
        <option value="1">Снять</option>
      </select>
    </div>

    <div class="col-12 col-lg-2">
      <select
        class="form-select form-select-lg mb-3"
        aria-label=".form-select-lg example"
      >
        <option selected>Вторичка</option>
        <option value="1">Новостройки</option>
      </select>
    </div>

    <div class="col-12 col-lg-2">
      <select
        class="form-select form-select-lg mb-3"
        aria-label=".form-select-lg example"
      >
        <option selected>Комнаты</option>
        <option value="1">1-комнатная</option>
      </select>
    </div>

    <div class="col-12 col-lg-2">
      <select
        class="form-select form-select-lg mb-3"
        aria-label=".form-select-lg example"
      >
        <option selected>Цена</option>
        <option value="1">1100 р м*2</option>
      </select>
    </div>
    <div class="col-12 mt-4 text-center">
      <button style="height:3em" type="button" class="btn btn-primary">Показать 120 объявлений</button>
    </div>
  </div>
</template>


<style lang="scss" scoped>
  .box-filter{
    border-radius: 12px;
    padding-top: 3em;
    padding-bottom: 3em;
    background-color: #d4f0ff;
  }
</style>
