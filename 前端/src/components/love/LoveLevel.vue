<!-- 组件说明 -->
<template>
  <div class="love-level">
    <a-row>
      <a-col
        :xs="12"
        :lg="6"
        v-for="count in 9"
        :key="count"
        @click="active(count)"
        
      >
        <div class="love-level-cell" 
        :class="{ active: currentSort == count }">
          <a href="javascript:;" :class="'love-color-' + count"
          @click="selectLove(count)">
            <a-icon type="heart" theme="filled" />
            <span style="color: black">喜爱等级：{{ count }}</span>
          </a>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
//import x from ''
export default {
  components: {},
  data() {
    return {
      currentSort:0,
    };
  },
  computed: {},
  methods: {
    active(count) {
      this.currentSort = count;
    },
    selectLove(count) {
      let page = this.$route.query.page;
      let sortby = this.$route.query.sortby;
      console.log("count", count);
      this.$router.push({
        path: "love",
        query: {
          love_level: count,
          page: page,
          sortby,
        },
      });
    },
  },
};
</script>

<style lang='scss' scoped>
//@import url()
.love-level {
  margin: 0 auto;
  width: 80%;
  text-align: center;
  .ant-col {
    text-align: center;
    .love-level-cell {
      margin: 0 auto;
      text-align: center;
      width: 120px;
      border: 2px solid rgba($color: #eee, $alpha: 0);
      border-radius: 6px;
      a {
        margin-top: 50%;
        text-align: center;
      }
    }
  }
}

.active {
  box-sizing: border-box;
  border: 2px solid #eee;
  border-radius: 6px;
  background-color: #ccc;
}

.love-color-1 {
  color: red !important;
}
.love-color-2 {
  color: orange !important;
}
.love-color-3 {
  color: rgba(197, 197, 45, 1) !important;
}
.love-color-4 {
  color: green !important;
}
.love-color-5 {
  color: blue !important;
}
.love-color-6 {
  color: Indigo !important;
}
.love-color-7 {
  color: purple !important;
}
.love-color-8 {
  color: pink !important;
}
.love-color-9 {
  color: black !important;
}
</style>