<!-- 组件说明 -->
<template>
  <div class="pagination">
    <a-pagination v-model="current" :total="totalPage" :showQuickJumper="true"  
    :pageSize="36" 
    />
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: "Pagination",
  components: {},
  data() {
    return {
      current: "",
      totalPage:36
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
      set() {
        
      }
    }
  },

  methods: {
    getApi() {
      let _this = this;
      let urlQuery = this.$route.query;
      let pageNum = Number(urlQuery.page);
      _this.current = pageNum;
      // console.log("-----pageNum-----", pageNum);
      // console.log("---urlQuery----", urlQuery);
      //   axios.get("http://localhost:8080/api/"+pageNum+"/api").then(value => {
      //   console.log(value);
      //   // _this.indexData = value.data;
      //   // _this.videoIndex = value.data.videoIndex;
      //   // _this.pageList = value.data.pageList;
      //   // _this.curPage = value.data.curPage;
      // });
    }
  },
  watch: {
    current: function() {
      let _this = this;
      let changedCurrent = _this.current;
      console.log("changedCurrent=======Pagination", changedCurrent);
      _this.$store.commit("getChangedCurrent", changedCurrent);
    },
    indexData: function() {
      let _this = this;
      this.totalPage = _this.indexData.finalPage*36
    }
  }
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