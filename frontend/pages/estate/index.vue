<template>
<div>
  <span style="font-size: 2em">Обьявления</span>
  <div class="row">
    <div v-for="i in 12" class="col-12 mt-4">
      <AdsCard/>
    </div>
  </div>
</div>
</template>

<script>
export default {
  layout:'estate'
}
</script>
