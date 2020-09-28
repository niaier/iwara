<!-- 组件说明 -->
<template>
  <div class="container">
    <div class="video-list">
      <a-row>
        <a-col :xs="24" :md="12" :lg="8" :xl="6" v-for="(item,i) in indexData.pageLength" :key="i">
          <a-card style="width: 240px">
            <a :href="'/play/'+videoIndex[i].dirname" slot="cover">
              <div class="heart-view ">
                <div class="v-box-heart">
                  <a-icon type="heart" theme="filled" />
                  {{videoIndex[i].love}}
                </div>
                <div class="v-box-view">
                  <a-icon type="eye" />
                  {{videoIndex[i].views}}
                </div>
              </div>
                <!-- :src="'http://127.0.0.1:3000/video/'+videoIndex[i].dirname+'/'+videoIndex[i].dirname+'.jpg'" -->
              <img
                style="display:block;width:100%"

                :src="'http://192.168.50.221:3000/video/'+videoIndex[i].dirname+'/'+videoIndex[i].dirname+'.jpg'"
              />
            </a>

            <p>
              标题
              <a :href="'/play/'+videoIndex[i].dirname">{{videoIndex[i].title}}</a>
            </p>
            <p>
              作者
              <a href title="查看用户资料" class="username">{{videoIndex[i].producer}}</a>
            </p>
          </a-card>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
//import x from ''
const axios = require("axios");
export default {
  name: "VideoList",
  components: {},
  data() {
    return {
      indexData: "",
      totalCount:"",
    };
  },
  created() {
    this.getApi();
  },
  updated() {},
  computed: {
    changedCurrent: {
      get() {
        return this.$store.state.changedCurrent;
      },
      set(v) {
        this.countData = v;
      },
    },
  },

  methods: {
    getApi() {
      let _this = this;
      let urlQuery = _this.$route.query;
      let page = urlQuery.page;
      let sortby = urlQuery.sortby;
      console.log("videolist", urlQuery);
      axios
        .get("/videoList", {
          params: {
            page: page - 1,
            sortby,
          },
        })
        .then((value) => {
          console.log(value);
          _this.indexData = value.data;
          _this.videoIndex = value.data.videoIndex;
          _this.pageList = value.data.pageList;
          _this.curPage = value.data.curPage;
          _this.totalCount = value.data.totalCount;
          console.log('_this.totalCount-----------',_this.totalCount)
        });
        
    },
  },
  watch: {
    indexData: function () {
      let _this = this;
      let indexData = _this.indexData;
      console.log("发送indexData到state");
      _this.$store.commit("getIndexData", indexData);
    },
    $route: function () {
      console.log("路由改变");
      this.getApi();
    },
    totalCount: function () {
      let _this = this;
      let totalCount = _this.totalCount;
      console.log("发送totalCount到state");
      _this.$store.commit("getTotalCount", totalCount);
    }
  },
};
</script>

<style lang='scss' scoped>
//@import url()
div.container {
  width: 80%;
  margin: 0 auto;
}

div.video-list {
  position: relative;
  margin: 0 auto;
  background-color: #ccc;
  overflow: hidden;

  .ant-col {
    // position: absolute;
    // left: 50%;
    // translate: 50%;
    height: 280px;
    border: 3px solid #ccc;
    overflow: hidden;
    background-color: #fff;

    div.ant-card {
      margin: 0 auto;
      border: none!important;
      .ant-card-body {
        
        // border: 3px solid red;
      }

      .ant-card-cover img {
        vertical-align: middle;
        border-style: none;
        border-radius: 2px 2px 0 0;
      }
      .ant-card-cover {
        display: block;
        width: 100%;
        .heart-view {

          color: #eee;
          .v-box-heart {
            position: absolute;
            left: 2px;
          }
          .v-box-view {
            position: absolute;
            right: 2px;
          }
        }
      }
    }
  }
}
</style>