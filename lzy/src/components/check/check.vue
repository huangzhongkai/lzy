<template>
  <div class="content">
    <div class="waper">
      <input class="auth_input" v-model="auth" v-on:focus="focus" v-on:blur="blur">
    </div>
    <div class="commit">
      <button  @click="commit" type="button" class="btn btn-primary">防伪验证</button>
    </div>
    <div class="l">
      <span>©老中医</span>
    </div>

  </div>
</template>

<script type="text/ecmascript-6">

  export default{
    data () {
      return {
        auth:'请输入防伪码',
        code:0,
      }
    },
    methods: {
      focus() {
        if(this.auth==='请输入防伪码'){
            this.auth='';
        }
      },
      blur() {
        if(this.auth===''){
          this.auth='请输入防伪码';
        }
      },
      commit() {
        if(this.auth != '' && this.auth !='请输入防伪码')
        this.$http.get('http://10.50.101.66:8887/get_auth/?code='+ this.auth).then(response => {
          this.code = response.body.code;
          if(this.code === 0){
            alert('经系统验证，该产品为正品')
          }else if(this.code === -1){
            alert('经系统验证，您所查防伪码不存在，请谨防假冒！')
          }else if(this.code === 1){
            alert('经系统验证，您所查验证码已过期，请谨防假冒')
          }
//          window.open('http://10.50.101.66:8080/show/show.html?type=' + this.code)
        },response => {
        });
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
    background-image: url("/static/bg.jpg")
    background-size: 100% 100%
    .waper
      text-align: center
      vertical-align: middle
      margin-top: 10px
      .auth_input
        margin-top: 100px
        vertical-align: middle
        width: 300px
        height: 50px
        text-align: center
        border: 2px #000 solid;
    .commit
      text-align: center
      vertical-align: middle
      margin-top: 10px
    .l
      text-align: center
      vertical-align: middle
      margin-top: 10px
</style>
