<template>
  <div class="w-full h-10 flex gap-2">
    <button
      class="left bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 flex flex-col items-center justify-center"
      v-on:click.prevent="moveListToLeft"
    >
      <Icon name="fluent-mdl2:chevron-left" size="15" />
    </button>
    <button
      class="left bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 flex flex-col items-center justify-center"
      v-on:click.prevent="moveListToRight"
    >
      <Icon name="fluent-mdl2:chevron-right" size="15" />
    </button>
    <select
      name="limit"
      id="limit"
      class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 px-1 placeholder:text-teal-950/50"
      v-on:change.prevent="setListLimit"
    >
      <option v-bind:selected="props.limit === 10 ? true : false" value="10">10</option>
      <option v-bind:selected="props.limit === 25 ? true : false" value="25">25</option>
      <option v-bind:selected="props.limit === 50 ? true : false" value="50">50</option>
      <option v-bind:selected="props.limit === 75 ? true : false" value="75">75</option>
      <option v-bind:selected="props.limit === 100 ? true : false" value="100">100</option>
    </select>
  </div>
</template>
<script setup lang="ts">
const props = defineProps(["limit", "listUpdate", "limitUpdate"]);

// const state = reactive({ limit: props.limit });
// console.log(state.limit);

const setListLimit = (e: Event) => {
  /**
   * Set default limit of from parent element as props
   * Change pagination limit on event listener
   * Update displaying list from the store with props
   * Update function should be from parent element
   */
  const selectEl = e.target as HTMLSelectElement;
  const newLimit = parseInt(selectEl.value, 10);
  props.limitUpdate(newLimit);
};

const moveListToLeft = (e: Event) => {
  /**
   * Get limit from props
   * List of items currently displaying
   * Filter the list
   * Update current items displaying and Set it to store
   */
  props.listUpdate(true);
};

const moveListToRight = (e: Event) => {
  // Just revert function
  props.listUpdate(false);
};
</script>
