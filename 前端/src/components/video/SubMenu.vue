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
      this.$router.push({
        path: "/video",
        query: { page: page, sortby: "upload_time" },
      });
    },
    toSortLove() {
      let page = this.$route.query.page;
      this.$router.push({
        path: "/video",
        query: { page: page, sortby: "love" },
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



