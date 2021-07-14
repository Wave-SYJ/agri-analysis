const routes =  [
  {
    path: '/login',
    name: 'login',
    component: () => import("@/views/login")
  },
  {
    path: '/',
    name: 'root',
    redirect: '/dashboard/monitor'
  },
  {
    path: 'dashboard',
    name: 'dashboard',
    component: () => import("@/components/Layout"),
    children: [
      {
        path: '/dashboard/monitor',
        name: 'dashboard-monitor',
        component: () => import("@/views/monitor")
      },
      {
        path: '/dashboard/predict',
        name: 'dashboard-predict',
        component: () => import("@/views/predict")
      },
      {
        path: '/dashboard/find',
        name: 'dashboard-find',
        redirect: '/dashboard/find/region',
        children: [
          {
            path: '/dashboard/find/region',
            name: 'dashboard-find-region',
            component: () => import("@/views/find/region")
          },
          {
            path: '/dashboard/find/compare',
            name: 'dashboard-find-compare',
            component: () => import("@/views/find/compare")
          },
          {
            path: '/dashboard/find/sell',
            name: 'dashboard-find-sell',
            component: () => import("@/views/find/sell")
          }
        ]
      },
      {
        path: '/dashboard/admin',
        name: 'dashboard-admin',
        redirect: '/dashboard/admin/data',
        children: [
          {
            path: '/dashboard/admin/data',
            name: 'dashboard-admin-data',
            component: () => import("@/views/admin/data")
          },
          {
            path: '/dashboard/admin/user',
            name: 'dashboard-admin-user',
            component: () => import("@/views/admin/user")
          }
        ]
      }
    ]
  }
]

export default routes