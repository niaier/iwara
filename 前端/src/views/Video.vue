<template>
  <div>
    <SubMenu></SubMenu>
    <br />
    <Pagination></Pagination>
    <br />
    <VideoList></VideoList>
    <br />
    <Pagination></Pagination>
  </div>
</template>
<script>
import SubMenu from "../components/video/SubMenu.vue";
import VideoList from "../components/video/VideoList.vue";
import Pagination from "../components/video/Pagination.vue";

// import axios from 'axios'

export default {
  name: "Video",
  components: {
    SubMenu,
    VideoList,
    Pagination,
  },
  created() {},

  methods: {},
};
</script>




