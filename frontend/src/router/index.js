import { createRouter, createWebHistory } from 'vue-router'
import CoursesViewVue from '@/views/CoursesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'courselist',
      component: CoursesViewVue
    },
    {
      path: '/:courseId',
      name: 'coursedetail',
      component: () => import('../views/CourseDetailView.vue')
    }
  ]
})

export default router
