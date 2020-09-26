<!-- 组件说明 -->
<template>
  <div class>
    <a-row>
      <a-col
        :xs="{ span: 22, offset: 1 }"
        :lg="{ span: 18, offset: 3 }"
        :xl="{ span: 16, offset: 4 }"
        class="playbox"
      >
        <video ref="video" controls width="100%" :src="videoSrc"></video>
      </a-col>
    </a-row>
    <h1></h1>
  </div>
</template>

<script>
// import func from '../../../vue-temp/vue-editor-bridge';
//import x from ''
export default {
  // props:['videoInfo'],
  components: {

  },
  data() {
    return {
      videoSrc:""
    };
  },
  computed: {
    VideoInfo:function(){
      let videoInfo = this.$store.state.videoInfo;
      return videoInfo;
    }
  },
  methods: {
    getSrc(){
      // let dirname = this.$route.params.videoId;
      // this.videoSrc = "http://127.0.0.1:3000/video/"+dirname+'/'+this.$store.state.videoInfo.title+'.mp4'
      // console.log("this.videoSrc",this.videoSrc)
    }
  },
  created(){
    // this.getSrc();
  },
  watch: {
    VideoInfo:function(){
      let dirname = this.$route.params.videoId;
      let videoSrc = "http://127.0.0.1:3000/video/"+dirname+'/'+this.$store.state.videoInfo.title+'.mp4'
      this.videoSrc = videoSrc;
    }
  },
};
</script>

<style lang='scss' scoped>
//@import url()
.playbox {
  // width:100%;
  // margin: 0 auto;
  border: 2px solid red;
}
</style>