import Layout from '@/components/Layout'

export const dashboardRoutes = [
  {
    path: '/dashboard/monitor',
    name: 'dashboard-monitor',
    component: Layout,
    children: [{
      path: '/dashboard/monitor',
      component: () => import("@/views/monitor")
    }],
    meta: {
      title: '数据监控',
      icon: 'el-icon-view'
    }
  },
  {
    path: '/dashboard/predict',
    name: 'dashboard-predict',
    component: Layout,
    children: [{
      path: '/dashboard/predict',
      component: () => import("@/views/predict")
    }],
    meta: {
      title: '数据预测',
      icon: 'el-icon-data-line'
    }
  },
  {
    path: '/dashboard/find',
    name: 'dashboard-find',
    redirect: '/dashboard/find/region',
    meta: {
      title: '数据查询',
      icon: 'el-icon-search',
      hasChildren: true
    },
    component: Layout,
    children: [
      {
        path: '/dashboard/find/region',
        name: 'dashboard-find-region',
        component: () => import("@/views/find/region"),
        meta: {
          title: '区域行情',
          icon: 'el-icon-location-outline'
        },
      },
      {
        path: '/dashboard/find/compare',
        name: 'dashboard-find-compare',
        component: () => import("@/views/find/compare"),
        meta: {
          title: '品种对比',
          icon: 'el-icon-ship'
        },
      },
      {
        path: '/dashboard/find/sell',
        name: 'dashboard-find-sell',
        component: () => import("@/views/find/sell"),
        meta: {
          title: '售卖行情',
          icon: 'el-icon-cherry'
        },
      }
    ]
  },
  {
    path: '/dashboard/admin',
    name: 'dashboard-admin',
    redirect: '/dashboard/admin/data',
    meta: {
      title: '数据管理',
      icon: 'el-icon-edit',
      hasChildren: true
    },
    component: Layout,
    children: [
      {
        path: '/dashboard/admin/data',
        name: 'dashboard-admin-data',
        component: () => import("@/views/admin/data"),
        meta: {
          title: '数据修改',
          icon: 'el-icon-edit-outline'
        },
      },
      {
        path: '/dashboard/admin/user',
        name: 'dashboard-admin-user',
        component: () => import("@/views/admin/user"),
        meta: {
          title: '用户管理',
          icon: 'el-icon-user'
        },
      },
      {
        path: '/dashboard/admin/password',
        name: 'dashboard-admin-password',
        component: () => import("@/views/admin/password"),
        meta: {
          title: '修改密码',
          icon: 'el-icon-lock'
        }
      }
    ]
  }
]

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import("@/views/login")
  },
  {
    path: '/',
    name: 'root',
    redirect: '/dashboard'
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    redirect: '/dashboard/monitor'
  },
  ...dashboardRoutes
]

export default routes