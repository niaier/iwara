<template>
  <a-col :span="12" :offset="6" class="home-container">
    <h1>最近视频</h1>
    <a-col :span="12" class="cell">1</a-col>
    <a-col :span="12" class="cell">2</a-col>
    <a-col :span="12" class="cell">3</a-col>
    <a-col :span="12" class="cell">4</a-col>
    <a-col :span="12" class="cell">5</a-col>
    <a-col :span="12" class="cell">6</a-col>
    <h1>最近喜爱</h1>
    <a-col :span="12" class="cell">1</a-col>
    <a-col :span="12" class="cell">2</a-col>
    <a-col :span="12" class="cell">3</a-col>
    <a-col :span="12" class="cell">4</a-col>
    <a-col :span="12" class="cell">5</a-col>
    <a-col :span="12" class="cell">6</a-col>
  </a-col>
</template>
<script>
export default {
  data() {
    return {
      current: ["mail"],
    };
  },
};
</script>

<style lang="scss" scope>
.home-container {
  text-align: center;
  h1 {
    font-size: 41px;
  }
  .cell {
    background-color: #fff;
    border: solid 1px #ccc;
  }
}
</style>
