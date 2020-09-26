<!-- 组件说明 -->
<template>
  <div class>
    <a-row>
      <a-col
        :xs="{ span: 22, offset: 1 }"
        :lg="{ span: 18, offset: 3 }"
        :xl="{ span: 16, offset: 4 }"
        class="video-info"
      >
        <h1>{{VideoInfo.title}}</h1>
        <div class="heart-view clearfix">
          <div class="v-box-heart">
            <a-icon type="heart" theme="filled" />{{VideoInfo.love}}
            
            <!-- {{videoIndex[i].love}} -->
          </div>
          <div class="v-box-view">
            <a-icon type="eye" />{{VideoInfo.views}}
            <!-- {{videoIndex[i].views}} -->
          </div>
        </div>
        <br>
        <div>
          <span>
            制作者：
            <a href>{{VideoInfo.producer}}</a>
          </span>
          <span v-html="'&nbsp;&nbsp;&nbsp;&nbsp;'"></span>

          <span>上传时间：{{time}}</span>
        </div>

        <br />
        <div>{{VideoInfo.description}}</div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import rTime from "../../moudles/dateFormat.js";
console.log(rTime.rTime("2020-01-13T16:00:00.000Z"));
export default {
  components: {},
  data() {
    return {
      time: "",
    };
  },
  computed: {
    VideoInfo: function () {
      let videoInfo = this.$store.state.videoInfo;
      return videoInfo;
    },
  },
  created() {},
  watch: {
    VideoInfo: function () {
      console.log(this.VideoInfo.upload_time);
      this.time = rTime.rTime(this.VideoInfo.upload_time);
    },
  },
  methods: {},
};
</script>

<style lang='scss' scoped>
//@import url()\
.clearfix:before,
.clearfix:after {
  content: "";
  display: table;
}
.clearfix:after {
  clear: both;
}

.video-info {
  // min-height: 100px;
  border: 2px solid red;
  .heart-view {
    // height: 20px;
    // color: #eee;
    // position: relative;
    font-size: 1.2em;
    .v-box-heart {
      float: left;
      // position: absolute;
      // left: 2px;
    }
    .v-box-view {
      float: left;
      margin-left: 10px;
      // position: absolute;
      // right: 2px;
    }
  }
}
</style>