<script lang="ts">
  import { onMount } from 'svelte';

  interface User {
    id: number;
    name: string;
  }
  let users: User[] = [];
  let name = '';

  const apiUrl = import.meta.env.VITE_API_URL;

  async function fetchUsers() {
    const res = await fetch(`${apiUrl}/users`);
    users = await res.json();
  }

  async function addUser() {
    await fetch(`${apiUrl}/users?name=` + name, { method: 'POST' });
    name = '';
    await fetchUsers();
  }


  onMount(() => {
    fetchUsers();
  });
</script>

<main class="p-6">
  <h1 class="text-2xl font-bold mb-4">Users</h1>

  <div class="mb-4">
    <input bind:value={name} placeholder="Enter name" class="border p-2 mr-2" />
    <button on:click={addUser} class="bg-blue-500 text-white px-4 py-2">Add User</button>
  </div>

  <ul class="list-disc pl-5">
    {#each users as user}
      <li>{user.name}</li>
    {/each}
  </ul>
</main>
