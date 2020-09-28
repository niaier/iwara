<!-- 组件说明 -->
<template>
  <div class="pagination">
    <a-pagination
      v-model="current"
      :total="totalCount"
      :showQuickJumper="true"
      @change="
        (page) => {
          skipPage(page);
        }
      "
      :pageSize="36"
    />
  </div>
</template>

<script>
// import func from '../../../vue-temp/vue-editor-bridge';
// import axios from 'axios'
export default {
  name: "Pagination",
  components: {},
  data() {
    return {
      current: "",
      // totalPage: 36,
      // indexData: ""
    };
  },
  created() {
    this.getApi();
  },
  computed: {
    indexData: {
      get() {
        return this.$store.state.indexData;
      },
      set() {},
    },
    totalCount: {
      get() {
        return this.$store.state.totalCount;
      },
      set() {},
    },
  },

  methods: {
    getApi() {
      let _this = this;
      let urlQuery = this.$route.query;
      let pageNum = Number(urlQuery.page);
      _this.current = pageNum;
      console.log("-----pageNum-----", pageNum);
      console.log("---urlQuery----", urlQuery);
    },
    skipPage(page) {
      let _this = this;
      console.log("跳转页面", page);
      console.log("this", this);
      // let page = _this.changedCurrent;
      let sortby = _this.$route.query.sortby;
      this.$router.push({
        path: "/video",
        query: { page: page, sortby: sortby },
      });
    },
  },
  watch: {
    current: function () {
      // let _this = this;
      // let changedCurrent = _this.current;
      // console.log("changedCurrent=======Pagination", changedCurrent);
      // _this.$store.commit("getChangedCurrent", changedCurrent);
    },
    // indexData: function () {
    //   let _this = this;
    //   this.totalPage = _this.indexData.finalPage * 36;
    // },
    totalCount:function () {
      // let _this = this;
      console.log('this.$store.state.totalCount',this.$store.state.totalCount)
    }
  },
};
</script>

<style lang='scss' scoped>
//@import url()
div.pagination {
  ul.ant-pagination {
    // margin: 0 auto;
    text-align: center;
  }
}
</style>