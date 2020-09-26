<!-- 组件说明 -->
<template>
  <div class>
<SubMenu></SubMenu>
    <br>
    <LoveLevel></LoveLevel>
    <br />
    <SearchVideo></SearchVideo>
    <br />
    <VideoList></VideoList>
    <br>
    <Pagination></Pagination>
  </div>
</template>

<script>
//import x from ''
import  SubMenu from "../components/love/SubMenu";
import LoveLevel from "../components/love/LoveLevel";
import SearchVideo from "../components/love/SearchVideo";
import VideoList from '../components/love/VideoList';
import Pagination from '../components/love/Pagination';
export default {
  components: {
    SubMenu,
    LoveLevel,
    SearchVideo,
    VideoList,
    Pagination,
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
</style>