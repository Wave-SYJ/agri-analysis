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
        path: '/dashboard/b/a',
        component: () => import("@/views/b/a")
      },
      {
        path: '/dashboard/b/b',
        component: () => import("@/views/b/b")
      },
      {
        path: '/dashboard/b/c',
        component: () => import("@/views/b/c")
      },
      {
        path: '/dashboard/c',
        component: () => import("@/views/c")
      },
      {
        path: '/dashboard/d/a',
        component: () => import("@/views/d/a")
      },
      {
        path: '/dashboard/d/b',
        component: () => import("@/views/d/b")
      },
    ]
  }
]

export default routes