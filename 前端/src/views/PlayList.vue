<!-- 组件说明 -->
<template>
  <div class="play-list">
    <SubMenu></SubMenu>

    <a-row class="playlist-content clearfix">
        <a-col ><LeftMenu></LeftMenu></a-col>
    
      <a-col   :sm="24" :lg="17" class="playlist-view">
          <br>
        <LoveLevel></LoveLevel>
        <br />
        <SearchVideo></SearchVideo>
        <br />
        <VideoList></VideoList>
        <br />
        <Pagination></Pagination>
      </a-col>
    </a-row>
  </div>
</template>

<script>
//import x from ''
import SubMenu from "../components/playlist/SubMenu";
import LeftMenu from "../components/playlist/LeftMenu";
import LoveLevel from "../components/playlist/LoveLevel";
import SearchVideo from "../components/playlist/SearchVideo";
import VideoList from "../components/playlist/VideoList";
import Pagination from "../components/playlist/Pagination";
export default {
  components: {
    SubMenu,
    LoveLevel,
    SearchVideo,
    VideoList,
    Pagination,
    LeftMenu,
  },
  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>

<style lang='scss' scoped>
//@import url()
.playlist-content {
  height: 100%;
  background-color: #fff;
}

.playlist-view {
  margin-left: -0.8px;
//   width: 70%;
  float: left;
  border-left: 0.8px solid #e8e8e8;
}
.left-menu {
  float: left;
  height: 100%;
  background-color: #fff;
  ul{
      border-right:0!important;
  }
}
.clearfix:before,
.clearfix:after {
  content: "";
  display: table;
}
.clearfix:after {
  clear: both;
}
.clearfix {
  *zoom: 1;
}
</style>