<template>
  <div id="components-layout-demo-basic">
    <div id="sub-menu">
      <a-menu v-model="current" mode="horizontal">
        <a-menu-item id="sort-by" key="sort">Sort by:</a-menu-item>
        <a-menu-item key="date" @click="toSortDate">
Date
        </a-menu-item>
        <a-menu-item key="love"  @click="toSortLove">
          Love
        </a-menu-item>
      </a-menu>
    </div>
  </div>
</template>
<script>
export default {
  name: "SubMenu",
  data() {
    return {
      current: ["new"],
    };
  },
  methods: {
    toSortDate() {
      let page = this.$route.query.page;
      let love_level = this.$route.query.love_level;
      this.$router.push({
        path: "/love",
        query: { page: page, sortby: "upload_time",love_level },
      });
    },
    toSortLove() {
      let page = this.$route.query.page;
      let love_level = this.$route.query.love_level;
      this.$router.push({
        path: "/love",
        query: { page: page, sortby: "love",love_level },
      });
    },
  },
};
</script>

<style lang="scss" scope>
#sub-menu {
  ul {
    background: #444;
    border: 0;
    color: #fff;
  }
}

#sort-by {
  color: #fff !important;
  border-bottom: #fff !important;
  cursor: text;
}
</style>



