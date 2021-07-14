const routes =  [
  {
    path: '/login',
    component: () => import("@/views/login")
  },
  {
    path: '/',
    redirect: '/dashboard/monitor'
  },
  {
    path: 'dashboard',
    component: () => import("@/components/Layout"),
    children: [
      {
        path: '/dashboard/monitor',
        component: () => import("@/views/monitor")
      },
      {
        path: '/dashboard/query',
        component: () => import("@/views/query")
      }
    ]
  }
]

export default routes