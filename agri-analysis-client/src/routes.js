const routes =  [
  {
    path: '/login',
    component: () => import("@/views/login")
  },
  {
    path: '/',
    redirect: '/dashboard/a'
  },
  {
    path: 'dashboard',
    component: () => import("@/components/Layout"),
    children: [
      {
        path: '/dashboard/a',
        component: () => import("@/views/a")
      },
      {
        path: '/dashboard/b',
        component: () => import("@/views/b")
      }
    ]
  }
]

export default routes