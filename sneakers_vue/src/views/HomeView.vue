<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to ArnalIman Sneakers Shop
            </p>
            <p class="subtitle">
                The best sneakers shop online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <SneakersBox
        v-for="sneakers in latestSneakers"
        v-bind:key="sneakers.id"
        v-bind:sneakers="sneakers" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import SneakersBox from '@/components/SneakersBox'

export default {
  name: 'Home',
  data() {
    return {
      latestSneakers: []
    }
  },
  components: {
    SneakersBox
  },
  mounted() {
    this.getLatestSneakers()

    document.title = 'Home | Sneakers'
  },
  methods: {
    async getLatestSneakers() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-sneakers/')
        .then(response => {
          this.latestSneakers = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>
