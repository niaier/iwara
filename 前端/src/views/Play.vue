<!-- 组件说明 -->
<template>
  <div class>
    <br />
    <PlayContainer  ></PlayContainer>
    <br />
    <VideoInfo></VideoInfo>
    <br />
    <UserFunction></UserFunction>
  </div>
</template>

<script>
import axios from 'axios'
import PlayContainer from "../components/play/PlayContainer.vue";
import VideoInfo from "../components/play/VideoInfo.vue";
import UserFunction from "../components/play/UserFunction.vue";
export default {
  name: "Play",
  components: {
    PlayContainer,
    VideoInfo,
    UserFunction,
  },
  data() {
    return {
      videoInfo:''
    };
  },
  computed: {},
  methods: {
    getApi() {
      let _this = this;
      let urlParams= _this.$route.params;
      console.log(urlParams);
      axios.get('http://localhost:8080/api/'+'video/'+urlParams.videoId+'/loadVideoInfo').then(value => {
        console.log("loadVideoInfo",value)
        _this.videoInfo = value.data;
       _this.$store.commit("getVideoInfo", _this.videoInfo);
      })

    },
  },
  // beforeCreate(){
  //   this.getApi();
  // },
  created() {
    this.getApi();
  },
};
</script>

<style lang='scss' scoped>
//@import url()
</style>