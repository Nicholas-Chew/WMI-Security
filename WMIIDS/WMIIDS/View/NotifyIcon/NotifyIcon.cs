using System.ComponentModel;
using System.Windows;
using System.Windows.Forms;

namespace WMIIDS
{
    public partial class App : System.Windows.Application
    {
        private System.Windows.Forms.NotifyIcon notifyIcon;
        private bool isExit;

        public void NotifyBallonTip(string notifyTitle, string notifyText, ToolTipIcon topIcon, int timeout)
        {
            notifyIcon.BalloonTipText = notifyText;
            notifyIcon.BalloonTipIcon = topIcon;
            notifyIcon.BalloonTipTitle = notifyTitle;
            notifyIcon.ShowBalloonTip(timeout);
        }

        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);
            MainWindow = new WMIIDS.View.WMIIDS();
            MainWindow.Closing += MainWindow_Closing;

            CreateNotifyIcon();
        }

        private void CreateNotifyIcon()
        {
            notifyIcon = new System.Windows.Forms.NotifyIcon();
            notifyIcon.DoubleClick += (s, args) => ShowMainWindow();
            notifyIcon.Icon = new System.Drawing.Icon("Resource/Image/test.ico");
            notifyIcon.Text = "WMIIDS";
            notifyIcon.Visible = true;

            CreateContextMenu();
        }

        private void CreateContextMenu()
        {
            notifyIcon.ContextMenuStrip = new System.Windows.Forms.ContextMenuStrip();
            notifyIcon.ContextMenuStrip.Items.Add("Open WMI IDS").Click += (s, e) => ShowMainWindow();
            notifyIcon.ContextMenuStrip.Items.Add(new ToolStripSeparator());
            notifyIcon.ContextMenuStrip.Items.Add("Exit").Click += (s, e) => ExitApplication();
        }

        private void ShowMainWindow()
        {
            if (MainWindow.IsVisible)
            {
                if (MainWindow.WindowState == WindowState.Minimized)
                {
                    MainWindow.WindowState = WindowState.Normal;
                }
                MainWindow.Activate();
            }
            else
            {
                MainWindow.Show();
            }
        }

        private void ExitApplication()
        {
            isExit = true;
            MainWindow.Close();
            notifyIcon.Dispose();
            notifyIcon = null;
        }

        private void MainWindow_Closing(object sender, CancelEventArgs e)
        {
            if (!isExit)
            {
                e.Cancel = true;
                MainWindow.Hide();
            }
        }
    }
}
