<template>
  <div class="content">
    <div class="logo">
      <img src="http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/logo.png"/>
    </div>
    <div class="waper">
      <input class="auth_input" v-model="auth" v-on:focus="focus" v-on:blur="blur">
    </div>
    <div class="commit">
      <button  @click="commit" type="button" class="b btn btn-primary">防伪查询</button>
    </div>
    <div class="l">
      <span>©老中医</span>
    </div>

  </div>
</template>
b
<script type="text/ecmascript-6">

  export default{
    data () {
      return {
        auth:'请输入您要查询的防伪码',
        code:0,
      }
    },
    methods: {
      focus() {
        if(this.auth==='请输入您要查询的防伪码'){
            this.auth='';
        }
      },
      blur() {
        if(this.auth===''){
          this.auth='请输入您要查询的防伪码';
        }
      },
      commit() {
        if(this.auth != '' && this.auth !='请输入您要查询的防伪码'){
          this.$http.get('http://lzy.shyuying.info/get_auth/?code='+ this.auth).then(response => {
            this.code = response.body.code;
            if(this.code === 0){
              alert('您好，您所查询的商品是老中医正品，优质品质，谨防假冒!')
            }else if(this.code === -1){
              alert('经系统验证，您所查防伪码不存在，请谨防假冒！')
            }else if(this.code === 1){
              alert('经系统验证，您所查验证码已过期，请谨防假冒')
            }
//          window.open('http://10.50.101.66:8080/show/show.html?type=' + this.code)
          },response => {
          });
        }else{
          alert('请输入防伪码');
        }

      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  html,body,#app
    height: 100%
  .content
    width: 100%
    height: 100%
    background-image: url("http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/checkbg.jpg")
    background-size: 100% 100%
    background-
    .logo
      position: relative
      text-align: center
      top: 60px
      img
        width: 150px
        height: 80px
    .waper
      position: relative
      text-align: center
      top: -20px
      .auth_input
        margin-top: 100px
        vertical-align: middle
        width: 200px
        height: 35px
        border-radius: 10px
        text-align: center
        border: 1px #000 solid;
    .commit
      position: relative
      text-align: center
      top: 30px
      .b
        width: 200px
        border-radius: 20px
    .l
      text-align: center
      vertical-align: middle
      margin-top: 40px
</style>
